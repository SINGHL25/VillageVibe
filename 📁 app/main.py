import streamlit as st
from village_profile import village_info

from app.agriculture import agri_tips
from app.market_zone import market_view
from app.media_gallery import show_gallery
from app.events import show_events
from app.ai_bot import village_bot

st.set_page_config(page_title="VillageVibe", layout="wide")

st.title("🏡 VillageVibe - Discover Rural Culture & Products")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Villages", "Agriculture", "Market", "Media", "Events", "AI Assistant"
])

with tab1: village_info()
with tab2: agri_tips()
with tab3: market_view()
with tab4: show_gallery()
with tab5: show_events()
with tab6: village_bot()

