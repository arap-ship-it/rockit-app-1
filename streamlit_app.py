import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/🎸music.py"
)
sales = st.Page(
    "views/sales.py"
)
chat = st.Page(
    "views/botchat.py"
)
contact = st.Page(
    "views/contact.py" 
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




# --- RUN NAVIGATION ---
pg.run()
