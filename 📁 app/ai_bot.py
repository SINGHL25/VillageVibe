import streamlit as st

def village_bot():
    st.subheader("🤖 AI Assistant (Demo)")
    query = st.text_input("Ask about village, crops, or tradition")

    if query:
        if "rampur" in query.lower():
            st.info("Rampur is famous for sugarcane and handmade pottery.")
        elif "festival" in query.lower():
            st.info("Holi, Diwali, and Teej are celebrated with fairs and dance.")
        else:
            st.warning("AI model not integrated. Add GPT/OpenAI later.")

