import streamlit as st 

c1, c2 = st.columns(2)

with c1 :
    
    st.image("254c7d3e4737995ddd5292a3450f70ca.jpg") 
    st.title("ALL ABOUT TYPE SHI") 
    st.write(""" 
    - All About Movie 
    - All About Music
    - All About Good Stuff """) 
import streamlit as st 

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")
    st.balloons() 
            
              

