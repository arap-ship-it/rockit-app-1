import streamlit as st

pages = [
    st.Page(home, title="Home", icon="🏠"),
    st.Page(about, title="About", icon="ℹ️"),
]
pg = st.navigation(pages)
pg.run()
