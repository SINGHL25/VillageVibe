import streamlit as st
import os

def show_gallery():
    st.subheader("📸 Village Gallery")
    for file in os.listdir("assets/images"):
        if file.endswith(".jpg") or file.endswith(".png"):
            st.image(f"assets/images/{file}", width=400, caption=file)

