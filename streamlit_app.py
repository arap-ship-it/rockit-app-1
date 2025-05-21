import streamlit as st
rockit-app-1
├── streamlit_app.py
└── pages/
    ├── 1_Home.py
    └── 2_About.py
pages = [
    st.Page("Home", title="Home", icon="🏠"),
    st.Page("About", title="About", icon="ℹ️"),
]
pg = st.navigation(pages)
pg.run("rockit-app-1")
