import streamlit as st
import time

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

with location_tab:
    st.header("📍 Location")
    st.map({"lat": [41.2995], "lon": [69.2401]})
    st.success("Uzbekistan, Tashkent")

with contact_tab:
    st.header("📞 Contact Information")
    st.success("**Phone:** +998 91 339 44 54")
    st.warning("**Email:** shokhrukhmirzo_usmonov@student.itpu.uz")
    st.info("**Address:** Tashkent, Uzbekistan")

with ask_us_tab:
    st.header("💬 Ask a Question")

    st.write("💡 **Example questions you can try:**")
    st.markdown(
        "- What are your working hours?\n"
        "- Where is your location?\n"
        "- What is your phone number?\n"
        "- What is your email address?\n"
        "- How can I contact you?"
    )

    question = st.text_area("Type your question here:", placeholder="e.g., What are your working hours?")

    default_answers = {
        "hours": "Our working hours are Monday to Friday: 9 AM – 6 PM, Saturday: 10 AM – 4 PM, Sunday: Closed.",
        "location": "We are located in Tashkent, Uzbekistan.",
        "phone": "You can call us at +998 91 339 44 54.",
        "email": "You can email us at shokhrukhmirzo_usmonov@student.itpu.uz.",
        "contact": "Phone: +998 91 339 44 54, Email: shokhrukhmirzo_usmonov@student.itpu.uz."
    }

    if st.button("Submit Question"):
        with st.spinner("Checking for an answer..."):
            time.sleep(2)

        q_lower = question.lower()

        placeholder = st.empty()
        answer_text = ""

        if "hour" in q_lower or "time" in q_lower:
            answer_text = default_answers["hours"]
        elif "location" in q_lower or "where" in q_lower:
            answer_text = default_answers["location"]
        elif "phone" in q_lower or "call" in q_lower:
            answer_text = default_answers["phone"]
        elif "email" in q_lower or "mail" in q_lower:
            answer_text = default_answers["email"]
        elif "contact" in q_lower:
            answer_text = default_answers["contact"]
        else:
            st.warning("❌ Sorry, we don't have an exact answer for that at the moment.")
            st.markdown("[🚨 Raise a support ticket here (GitHub Issues)](https://github.com/usmonovshohruxmirzo/streamlit-app/issues/new)", unsafe_allow_html=True)
            st.stop()

        typed = ""

        for char in answer_text:
            typed += char
            placeholder.success(f"💬 {typed}")
            time.sleep(0.02)
