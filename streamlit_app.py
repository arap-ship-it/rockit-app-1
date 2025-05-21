import streamlit as st
your-app/
├── streamlit_app.py
└── pages/
    ├── 1_Home.py
    └── 2_About.py
pages = [
    st.Page(home, title="Home", icon="🏠"),
    st.Page(about, title="About", icon="ℹ️"),
]
pg = st.navigation(pages)
pg.run()
