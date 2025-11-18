import streamlit as st

# -------------------- PAGE TITLE --------------------
st.title("🏙️ A REAL ESTATE PROJECT")

# -------------------- INTRODUCTION SECTION --------------------
st.markdown("""
### 🏡 Welcome to the **Gurgaon Real Estate Price Prediction System**

This project helps users to **estimate property prices** in Gurgaon using advanced **Machine Learning (ML) models** trained on real housing data.

The dataset was scraped from the **99acres** website in **2023**, specifically for Gurgaon properties.  
Since prices change over time — with market fluctuations up to **67% price surge since 2023** —  
the system predicts a **realistic price range** instead of an exact number.  

Each model has been **carefully trained** to provide **reliable and consistent predictions** based on property attributes.

It consists of **two major components:**

---

### 1️⃣ Property Price Predictor Page

Here, you can enter key property details like:

- 🏠 Property Type (Flat / House)  
- 📏 Built-up Area (sq.ft)  
- 🛏️ Bedrooms  
- 🚿 Bathrooms  
- 🌇 Balconies  
- 🧹 Servant Room / 📦 Store Room  
- 📅 Property Age  
- 💎 Luxury Category  
- 🏢 Floor Category  
- 📍 Sector  

After entering these details, the system uses **three powerful ML models** to estimate the property price in **crores (₹ Cr)**.

---
""")

# -------------------- MODEL COMPARISON SECTION --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### 🌲 Random Forest  
    A stable ensemble model that blends multiple decision trees to produce balanced predictions.

    **Performance:**  
    - **R² Score:** 0.8327  
    - **MAE:** 0.52  
    - **Accuracy:** 83.27%
    """)

with col2:
    st.markdown("""
    ### ⚡ XGBoost  
    A fast and highly accurate boosting algorithm that captures complex patterns in housing data.

    **Performance:**  
    - **R² Score:** 0.90  
    - **MAE:** 0.45  
    - **Accuracy:** 85.27%
    """)

with col3:
    st.markdown("""
    ### 🌳 Extra Trees  
    A very fast, highly randomized forest model that handles non-linear relationships extremely well.

    **Performance:**  
    - **R² Score:** 0.90  
    - **MAE:** 0.4595  
    - **Accuracy:** 85.02%
    """)

st.markdown("---")
st.markdown("""
Together, these three models help create a **more reliable, stable, and realistic price prediction** for Gurgaon properties.
""")

# -------------------- ANALYTICS DASHBOARD INTRO --------------------
st.markdown("""
## 2️⃣ Analytics Dashboard Page

This dashboard helps you **analyze, visualize, and interpret** Gurgaon’s housing market using interactive data visualizations.  
You can explore **sector-wise trends**, **property features**, and **price behaviors** — all in one place!  

Here’s what each tab offers:
""")

# -------------------- DASHBOARD TAB DESCRIPTIONS --------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ 🌍 Geo Price Map")
    st.markdown("""
    Explore the **average property price per sqft** across all sectors of Gurgaon.  
    - Darker sectors indicate **higher prices**.  
    - Hover over any location to view **sector details**, including **average built-up area** and **price insights**.  
    - Quickly identify **real estate hotspots** across the city.
    """)

    st.subheader("2️⃣ ☁️ Sector-wise WordCloud")
    st.markdown("""
    Discover the **most common property features** in each sector.  
    - Select a **sector** and filter by **property type** (Flat / House).  
    - The word cloud visually highlights **popular features** in that region.  
    - A **Top 20 Features Bar Chart** is also displayed for quick comparison.
    """)

    st.subheader("3️⃣ 📈 Price Analysis")
    st.markdown("""
    Understand how **price varies** with different property attributes through **interactive plots**.

    **Sub-tabs:**
    - **3.1 Price Scatter:**  
      Visualize **Price vs. Feature** to explore relationships and trends.  
      Filter by **property type** to view patterns for flats or houses.  

    - **3.2 Price Distribution (KDE):**  
      View **price density and spread** across properties.  
      Analyze how prices cluster around specific ranges or features.  

    - **3.3 Correlation Heatmap:**  
      Explore **numeric relationships** between key features (e.g., area, price, rooms).  
      Identify which features most strongly **influence property prices**.
    """)

with col2:
    st.subheader("4️⃣ 🥧 BHK Distribution (Pie Chart)")
    st.markdown("""
    See how **different BHK types** (1BHK to 10BHK) are distributed across sectors.  
    - Filter by **sector** to focus on a specific area.  
    - Helps identify **property availability patterns** and **buyer preferences** in Gurgaon.
    """)

    st.subheader("5️⃣ 📦 BHK Price Comparison (Box Plot)")
    st.markdown("""
    Compare **price variations across BHK configurations**.  
    - View **median**, **minimum**, **maximum**, and **outliers** for each BHK type.  
    - Understand **price gaps** between 1BHK, 2BHK, 3BHK, and 4BHK properties.  
    - Ideal for identifying **value-for-money property categories**.
    """)

# -------------------- FOOTER / CREDITS --------------------
st.markdown("---")
st.markdown("""
### 💡 Conclusion  
This dashboard provides **data-driven insights** that empower investors, buyers, and researchers to make **informed real estate decisions**.  
Dive into each tab, apply filters, and uncover the **hidden stories** behind Gurgaon’s property prices and trends! 🏙️✨
""")

st.markdown("""
---
### 👨‍💻 **Project Developed By:** [**Mohammad Areeb**](https://www.linkedin.com/in/mohammad-areeb-uddin-4274622a2/)

**🔗 Connect with me:**  
- 💼 [LinkedIn](https://www.linkedin.com/in/mohammad-areeb-uddin-4274622a2/)  
- 🧠 [GitHub](https://github.com/AREEB-08)

🚀 *Thank you for exploring the Gurgaon Real Estate Price Prediction System!*
""")
