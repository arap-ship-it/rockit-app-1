import streamlit as st

st.page("streamlit_app.py", label="Home", icon="🏠")
st.page("page_1.py", label="Page 1", icon="1️⃣")
st.page("page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page("http://www.google.com", label="Google", icon="🌎")
