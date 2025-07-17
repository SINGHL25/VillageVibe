import streamlit as st
import json

def village_info():
    st.subheader("🏞️ Village Profiles")
    with open("data/villages.json") as f:
        villages = json.load(f)

    village = st.selectbox("Select a Village", list(villages.keys()))
    st.json(villages[village])

