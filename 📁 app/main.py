import os
import sys
import streamlit as st

# Ensure the current file's directory is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "app")))

# Import modules
from village_profile import village_info
from agriculture import agri_tips
from market_zone import market_view
from media_gallery import show_gallery
from events import show_events
from ai_bot import village_bot

# App UI
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

