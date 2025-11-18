import streamlit as st
import pickle
import pandas as pd
import numpy as np
import joblib

# ---------------------------------------
# PAGE TITLE
# ---------------------------------------
st.set_page_config(page_title="Gurgaon House Price Predictor", layout="wide")
st.title("🏡 **Gurgaon Property Price Prediction App**")
st.write("Enter property details below to get an accurate price prediction using multiple ML models.")

# ---------------------------------------
# LOAD PICKLE FILES
# ---------------------------------------
@st.cache_resource
def load_models():
    df = pickle.load(open(r'D:/PREDICTION_MODEL/datasets/df.pkl', 'rb'))
    rf = pickle.load(open(r'D:/PREDICTION_MODEL/models/RANDOM_FOREST_pipeline.pkl', 'rb'))
    xgb = joblib.load(r'D:/PREDICTION_MODEL/models/XGB_full_pipeline.pkl')
    ext = joblib.load(r'D:/PREDICTION_MODEL/models/EXTRA_TREES_full_pipeline.pkl')

    return df, rf, xgb, ext



df, rf_model, xgb_model, ext_model = load_models()

# st.dataframe(df)
# ---------------------------------------
# YES/NO FUNCTION
# ---------------------------------------
def yes_no_to_binary(value):
    return 1.0 if value == "Yes" else 0.0

# ---------------------------------------
# INPUT FORM
# ---------------------------------------
st.header("📝 Enter Property Details")

col1, col2, col3 = st.columns(3)

with col1:
    property_type = st.selectbox("🏠 Property Type", ['flat', 'house'])
    bedrooms = st.selectbox("🛏️ Number of Bedrooms", sorted(df['bedRoom'].unique().tolist()))
    bathroom = st.selectbox("🚿 Number of Bathrooms", sorted(df['bathroom'].unique().tolist()))
    balcony = st.selectbox("🌇 Number of Balconies", sorted(df['balcony'].unique().tolist()))

with col2:
    sector = st.selectbox("📍 Sector", sorted(df['sector'].unique().tolist()))
    property_age = st.selectbox("📅 Property Age", sorted(df['agePossession'].unique().tolist()))
    built_up_area = st.number_input("📐 Built-up Area (sq.ft)", step=10.0, min_value=100.0)

with col3:
    servant_room = st.selectbox("🧹 Servant Room", ["No", "Yes"])
    store_room = st.selectbox("📦 Store Room", ["No", "Yes"])
    furnishing_type = st.selectbox("🛋️ Furnishing Type", sorted(df['furnishing_type'].unique().tolist()))
    luxury_category = st.selectbox("💎 Luxury Category", sorted(df['luxury_category'].unique().tolist()))
    floor_category = st.selectbox("🏢 Floor Category", sorted(df['floor_category'].unique().tolist()))

# Convert Yes/No to 0/1
servant_room = yes_no_to_binary(servant_room)
store_room = yes_no_to_binary(store_room)

# ---------------------------------------
# PREDICTION
# ---------------------------------------
if st.button("🔍 Predict Price"):

    # Form DataFrame
    input_data = pd.DataFrame([[
        property_type, sector, bedrooms, bathroom, balcony, property_age,
        built_up_area, servant_room, store_room, furnishing_type,
        luxury_category, floor_category
    ]], columns=[
        'property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
        'agePossession', 'built_up_area', 'servant room', 'store room',
        'furnishing_type', 'luxury_category', 'floor_category'
    ])

    st.subheader("✅ Your Input Summary")
    st.dataframe(input_data, use_container_width=True)

    # ---------------------------------------
    # FUNCTION FOR PREDICTION
    # ---------------------------------------
    def predict_price(model, df):
        price = np.expm1(model.predict(df))[0]
        return round(price - 0.22, 2), round(price + 0.22, 2)


    # Note section
    st.info("""
    **📌 Important Note:**  
    This model is trained on **2023 scraped real-estate data**.  
    Actual market prices may vary due to changes in demand, sector development, builder pricing, and market fluctuations.
    """)

    st.markdown("---")
    st.header("📈 Predictions")

    # Random Forest
    rf_low, rf_high = predict_price(rf_model, input_data)
    st.success(f"🌲 **Random Forest Estimate:** {rf_low} Cr – {rf_high} Cr")

    # XGBoost
    xgb_low, xgb_high = predict_price(xgb_model, input_data)
    st.info(f"⚡ **XGBoost Estimate:** {xgb_low} Cr – {xgb_high} Cr")

    # Extra Trees
    ext_low, ext_high = predict_price(ext_model, input_data)
    st.warning(f"🌳 **Extra Trees Estimate:** {ext_low} Cr – {ext_high} Cr")

    st.markdown("---")
    st.write("✅ All predictions include the ±0.22 Cr uncertainty margin.")

