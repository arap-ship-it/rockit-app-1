import streamlit as st

pages = [
    st.Page("page_1.py", home, title="Home", icon="🏠"),
    st.Page("page_2.py", about, title="About", icon="ℹ️"),
]
pg = st.navigation(pages)
pg.run()
