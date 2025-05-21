import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/🏛️home.py"
)
sales = st.Page(
    "views/🎸music.py"
)
chat = st.Page(
    "views/🎬movie.py"
)
contact = st.Page(
    "views/luckystrike.py" 
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
