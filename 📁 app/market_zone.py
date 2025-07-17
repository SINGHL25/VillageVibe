import pandas as pd
import streamlit as st

def market_view():
    st.subheader("🛍️ Regional Product Market")
    df = pd.read_csv("data/products.csv")
    st.dataframe(df)

    product = st.selectbox("Product Name", df["Product Name"].unique())
    st.write(df[df["Product Name"] == product])

