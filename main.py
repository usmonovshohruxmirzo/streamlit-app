import streamlit as st

st.set_page_config(page_title="Business Info", page_icon="💼", layout="wide")

overview_tab, working_hours_tab, location_tab, contact_tab, ask_us_tab = st.tabs(["🏢 Overview", "⏰ Working Hours", "📍 Location", "📞 Contact", "💬 Ask Us"])
