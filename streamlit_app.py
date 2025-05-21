import streamlit as st
your-app/
├── streamlit_app.py
└── pages/
    ├── 1Home.py
    └── 2About.py
pages = [
    st.Page(Home, title="Home", icon="🏠"),
    st.Page(About, title="About", icon="ℹ️"),
]
pg = st.navigation(pages)
pg.run()
