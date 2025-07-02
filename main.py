import streamlit as st

st.set_page_config(page_title="Business Info", page_icon="💼", layout="wide")

overview_tab, working_hours_tab, location_tab, contact_tab, ask_us_tab = st.tabs(["🏢 Overview", "⏰ Working Hours", "📍 Location", "📞 Contact", "💬 Ask Us"])

with overview_tab:
    st.header("💼 Our Business at a Glance")
    st.metric("Clients", "1,200+", "🔥")
    st.metric("Years Active", "5+", "✅")
    st.metric("Rating", "4.9 ⭐", "👍")
    st.success("We provide high-quality IT solutions in Uzbekistan and worldwide.")

    st.subheader("📈 Client Growth Over Years")
    client_growth_data = {
        "Year": ["2019", "2020", "2021", "2022", "2023"],
        "Clients": [150, 300, 600, 900, 1200]
    }
    st.line_chart(client_growth_data, x="Year", y="Clients")

    st.subheader("💰 Revenue Distribution (in $K)")
    revenue_data = {
        "Year": ["2019", "2020", "2021", "2022", "2023"],
        "Revenue": [50, 120, 250, 400, 550]
    }
    st.bar_chart(revenue_data, x="Year", y="Revenue")

    st.subheader("🌟 Service Satisfaction Trend")
    satisfaction_data = {
        "Year": ["2019", "2020", "2021", "2022", "2023"],
        "Satisfaction": [80, 85, 88, 90, 95]
    }
    st.area_chart(satisfaction_data, x="Year", y="Satisfaction")

with working_hours_tab:
    st.header("⏰ Working Hours")
    st.info("**Monday to Friday:** 9 AM – 6 PM")
    st.info("**Saturday:** 10 AM – 4 PM ")
    st.info("**Sunday:** Closed")