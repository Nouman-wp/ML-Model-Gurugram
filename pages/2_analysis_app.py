import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import ast
from wordcloud import WordCloud

st.title("🤖 Page 2 – Analytics Dashboard")

# -------------------------------------------------------------------------------------
# Load Datasets
# -------------------------------------------------------------------------------------
new_df = pd.read_csv(r"D:/PREDICTION_MODEL/datasets/data_viz1.csv")
wordcloud_df = pd.read_csv(r"D:/PREDICTION_MODEL/datasets/word_cloud_data.csv")


numeric_cols = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df.groupby('sector')[numeric_cols].mean().reset_index()

# -------------------------------------------------------------------------------------
# Create Main Tabs
# -------------------------------------------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🌍 Geo Price Map",
    "☁️ WordCloud",
    "📈 Price Analysis",
    "🥧 BHK Pie Chart",
    "📦 BHK Price Comparison"
])

# =====================================================================================
# 🌍 TAB 1 — GEOMAP
# =====================================================================================
with tab1:
    st.header('Sector Price per Sqft - Geo Map')

    # Ensure numeric columns
    for col in ['latitude', 'longitude', 'price_per_sqft', 'built_up_area']:
        group_df[col] = pd.to_numeric(group_df[col], errors='coerce')

    # Drop rows with missing coordinates
    map_data = group_df.dropna(subset=['latitude', 'longitude'])
    # Rename columns for hover display
    map_data = map_data.rename(columns={

        'price_per_sqft': 'Mean Price per Sqft',
        'built_up_area': 'Mean Built-up Area'
    })


    # Create scatter_map with hover info
    fig = px.scatter_map(
        map_data,
        lat="latitude",
        lon="longitude",
        color='Mean Price per Sqft',
        size='Mean Built-up Area',
        color_continuous_scale=px.colors.cyclical.IceFire,
        zoom=10,
        map_style="open-street-map",
        hover_name='sector',
        hover_data={
            "sector": True,
            'Mean Price per Sqft': True,
            'Mean Built-up Area': True,
            "latitude": True,
            "longitude": True
        }
    )

    # Set fixed figure size
    fig.update_layout(
        height=900,
        width=1400
    )

    st.plotly_chart(fig, use_container_width=True)



# =====================================================================================
# ☁️ TAB 2 — WORDCLOUD (Updated)
# =====================================================================================

with tab2:
    st.header("Sector-wise WordCloud Generator")

    # Clean text columns
    wordcloud_df['sector'] = wordcloud_df['sector'].str.lower().str.strip()
    if 'property_type' in wordcloud_df.columns:
        wordcloud_df['property_type'] = wordcloud_df['property_type'].str.lower().str.strip()

    wordcloud_df['features'] = wordcloud_df['features'].apply(
        lambda x: ast.literal_eval(x) if isinstance(x, str) else x
    )

    # Filters
    col1, col2 = st.columns(2)
    with col1:
        sectors = ["overall"] + sorted(wordcloud_df['sector'].dropna().unique())
        selected_sector = st.selectbox("Select a Sector", sectors)
    with col2:
        property_types = ["overall"]
        if 'property_type' in wordcloud_df.columns:
            property_types += sorted(wordcloud_df['property_type'].dropna().unique())
        selected_property_type = st.selectbox("Select Property Type", property_types)

    # Apply filters
    sector_data = wordcloud_df.copy()
    if selected_sector != "overall":
        sector_data = sector_data[sector_data['sector'] == selected_sector]
    if selected_property_type != "overall" and 'property_type' in sector_data.columns:
        sector_data = sector_data[sector_data['property_type'] == selected_property_type]

    # Build features list
    features_list = []
    for item in sector_data['features']:
        if isinstance(item, list):
            for f in item:
                if isinstance(f, list):
                    features_list.extend([str(x) for x in f])
                else:
                    features_list.append(str(f))

    features_list = [f.strip() for f in features_list if f and f.strip()]

    if len(features_list) == 0:
        st.warning("No feature words available for this selection.")
    else:
        # WordCloud
        wc = WordCloud(width=800, height=500, background_color="white").generate(" ".join(features_list))
        fig_wc, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig_wc)

        # Top features bar chart
        st.subheader("📊 Top Features")
        feat_counts = pd.Series(features_list).value_counts().head(20).reset_index()
        feat_counts.columns = ['Feature', 'Count']
        fig6 = px.bar(
            feat_counts,
            x='Feature',
            y='Count',
            title="Top 20 Features",
            text='Count'
        )
        st.plotly_chart(fig6, use_container_width=True)

# =====================================================================================
# 📈 TAB 3 — PRICE ANALYSIS (with sub-tabs)
# =====================================================================================
with tab3:
    st.header("🏙️ Property Price Visualization Dashboard — Gurgaon")

    # Clean numeric-like columns
    for col in ['balcony', 'bathroom', 'bedRoom', 'floorNum']:
        new_df[col] = (
            new_df[col]
            .astype(str)
            .str.replace('+', '', regex=False)
            .astype(float)
        )

    # --- Create Sub-Tabs ---
    scatter_tab, dist_tab, corr_tab = st.tabs([
        "🔹 Price Scatter",
        "🔹 Price Distribution",
        "🔹 Correlation Analysis"
    ])

    # ---------------------------------------------------------------
    # SUB-TAB 1: SCATTER PLOTS (Updated)
    # ---------------------------------------------------------------
    with scatter_tab:
        st.subheader("📈 Scatter Plots — Understand How Price Changes with Features")

        property_filter = st.selectbox("Select Property Type:", ["Overall", "flat", "house"], key="scatter_filter")
        if property_filter == "Overall":
            df_tab = new_df.copy()
        else:
            df_tab = new_df[new_df["property_type"] == property_filter]

        # Convert price into crores for readability
        df_tab['price_crore'] = df_tab['price'] / 1e7

        feature_options = ['Overall', 'bathroom', 'balcony', 'floorNum', 'built_up_area', 'luxury_score', 'bedRoom']
        x_feature = st.selectbox("Select feature to plot against Price:", feature_options)

        if x_feature == "Overall":
            fig = px.histogram(
                df_tab,
                x='price_crore',
                nbins=50,
                title=f'Overall Price Distribution ({property_filter})',
                labels={'price_crore': 'Price (in Crores ₹)'}
            )
        else:
            fig = px.scatter(
                df_tab,
                x=x_feature,
                y='price_crore',
                color='bedRoom',
                trendline='ols',
                title=f'{x_feature} vs Price (in Crores) — {property_filter}',
                labels={x_feature: x_feature.capitalize(), 'price_crore': 'Price (in Crores ₹)'}
            )

        st.plotly_chart(fig, use_container_width=True)

    # ---------------------------------------------------------------
    # SUB-TAB 2: KDE / DISTRIBUTION
    # ---------------------------------------------------------------
    with dist_tab:
        st.subheader("📊 Price Distribution — Understand How Prices Are Spread")

        property_filter = st.selectbox("Select Property Type:", ["Overall", "flat", "house"], key="kde_filter")
        if property_filter == "Overall":
            df_tab = new_df.copy()
        else:
            df_tab = new_df[new_df["property_type"] == property_filter]

        feature_options = ['Overall', 'bathroom', 'balcony', 'floorNum', 'built_up_area', 'luxury_score', 'bedRoom']
        kde_feature = st.selectbox("Select feature for KDE Plot:", feature_options)

        fig_kde, ax = plt.subplots(figsize=(7, 4))
        if kde_feature == "Overall":
            sns.kdeplot(data=df_tab, x='price', fill=True, alpha=0.4, ax=ax)
            plt.title(f'Overall Price Distribution ({property_filter})')
        else:
            sns.kdeplot(data=df_tab, x='price', hue=kde_feature, fill=True, alpha=0.4, ax=ax)
            plt.title(f'Price Distribution by {kde_feature.capitalize()} ({property_filter})')

        plt.xlabel("Price (₹)")
        plt.ylabel("Density")
        st.pyplot(fig_kde)

    # ---------------------------------------------------------------
    # SUB-TAB 3: CORRELATION
    # ---------------------------------------------------------------
    with corr_tab:
        st.subheader("🧮 Correlation Heatmap — Numeric Feature Relationships")

        property_filter = st.selectbox("Select Property Type:", ["Overall", "flat", "house"], key="corr_filter")
        if property_filter == "Overall":
            df_tab = new_df.copy()
        else:
            df_tab = new_df[new_df["property_type"] == property_filter]

        numeric_cols = df_tab.select_dtypes(include='number').columns
        corr = df_tab[numeric_cols].corr()

        fig_corr, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
        plt.title(f"Correlation Heatmap ({property_filter})")
        st.pyplot(fig_corr)

# =====================================================================================
# 🥧 TAB 4 — PIE CHART
# =====================================================================================
with tab4:
    st.header('BHK Pie Chart')

    sector_options = ['overall'] + new_df['sector'].unique().tolist()
    selected_sector2 = st.selectbox('Select Sector', sector_options)

    if selected_sector2 == 'overall':
        fig2 = px.pie(new_df, names='bedRoom', title='BHK Distribution (Overall)')
    else:
        fig2 = px.pie(
            new_df[new_df['sector'] == selected_sector2],
            names='bedRoom',
            title=f'BHK Distribution — {selected_sector2}'
        )
    st.plotly_chart(fig2, use_container_width=True)

# =====================================================================================
# 📦 TAB 5 — BOX PLOT
# =====================================================================================
with tab5:
    st.header('Side-by-Side BHK Price Comparison')

    fig3 = px.box(
        new_df[new_df['bedRoom'] <= 4],
        x='bedRoom',
        y='price',
        title='BHK Price Range'
    )
    st.plotly_chart(fig3, use_container_width=True)
