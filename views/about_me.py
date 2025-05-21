import streamlit as st 

st.title("~BARUDAWGH~")
st.write(
    "BEJA KA BARUDAWGH ONE KOMANDO"
)
st.image("aleta02150.jpg")
st.balloons() 
st.badge("NO1")
import streamlit as st
st.text("Kelakuan Anak Kucai") 

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    import streamlit as st
