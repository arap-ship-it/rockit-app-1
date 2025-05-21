import streamlit as st 

c1, c2 = st.columns(2)

with c1 : import streamlit as st

st.title("Cek Angka Genap atau Ganjil")

angka = st.number_input("Masukkan sebuah angka:", step=1)

    if angka % 2 == 0:
        st.success(f"{angka} adalah angka Genap.")
    else:
        st.info(f"{angka} adalah angka Ganjil.")
          
