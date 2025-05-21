import streamlit as st 

c1, c2 = st.columns(2)

with c1 : import streamlit as st

# Inisialisasi angka rahasia di session_state
if "secret_number" not in st.session_state:
    import random
    st.session_state.secret_number = random.randint(1, 10)

st.title("Game Tebak Angka Sederhana")

guess = st.number_input("Masukkan tebakan angka (1-10):", min_value=1, max_value=10, step=1)
if st.button("Tebak"):
    if guess == st.session_state.secret_number:
        st.success("Tebakan kamu benar! 🎉")
        # Reset angka rahasia untuk permainan baru
        st.session_state.secret_number = random.randint(1, 10)
    else:
        st.warning("Tebakan salah, coba lagi!")

st.write("Tebak angka antara 1 sampai 10.")
          
          
