import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
sales = st.Page(
    "views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
chat = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",
)
contact = st.Page(
    "views/contact.py",
    title="Contact",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, sales, chat])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [sales, chat],
        "Contact": [contact]
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/ngodingseru.png")
#st.sidebar.markdown("Made with ❤️")


# --- RUN NAVIGATION ---
pg.run()
