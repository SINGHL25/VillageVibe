import streamlit as st
import json
import os

def village_info():
    st.subheader("🏞️ Village Profiles")

    # Use relative path handling to prevent errors
    data_path = os.path.join(os.path.dirname(__file__), "..", "📁data", "villages.json")
    
    try:
        with open(data_path, "r") as f:
            villages = json.load(f)

        village_names = [v["name"] for v in villages]
        selected_name = st.selectbox("Select a Village", village_names)

        # Display details for the selected village
        selected_village = next(v for v in villages if v["name"] == selected_name)
        st.json(selected_village)

    except FileNotFoundError:
        st.error("⚠️ 'villages.json' file not found in the data/ folder.")
    except json.JSONDecodeError:
        st.error("⚠️ Error decoding JSON data in 'villages.json'.")
