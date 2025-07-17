import streamlit as st

def agri_tips():
    st.subheader("🌾 Seasonal Agricultural Tips")

    season = st.selectbox("Choose Season", ["Kharif", "Rabi", "Zaid"])
    if season == "Kharif":
        st.write("- Best crops: Rice, Maize, Cotton")
        st.write("- Irrigate well after rains.")
    elif season == "Rabi":
        st.write("- Best crops: Wheat, Mustard, Gram")
        st.write("- Use compost before sowing.")
    else:
        st.write("- Short crops like watermelon, cucumber")

