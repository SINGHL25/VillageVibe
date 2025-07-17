import json
import streamlit as st

def show_events():
    st.subheader("🎉 Village Events & Functions")
    with open("data/events.json") as f:
        events = json.load(f)

    for ev in events:
        st.write(f"📅 {ev['date']} - {ev['name']}")
        st.write(f"📍 Village: {ev['village']}")
        st.write(f"📝 Details: {ev['description']}")
        st.markdown("---")

