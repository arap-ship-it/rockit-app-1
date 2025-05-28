import streamlit as st 

c1, c2 = st.columns(2)

with c1 : import streamlit as st

# Inisialisasi angka rahasia di session_state
if "secret_number" not in st.session_state:
    import random
    st.session_state.secret_number = random.randint(1, 50)

st.title("Tebak angka bomb anak kucai")

guess = st.number_input("Masukkan tebakan angka (1-50):", min_value=1, max_value=50, step=1)
if st.button("Tebak"):
    if guess == st.session_state.secret_number:
        st.success("Tebakan kamu benar! 🎉")
        st.balloons() 
        # Reset angka rahasia untuk permainan baru
        st.session_state.secret_number = random.randint(1,50)
    else:
        st.warning("Tebakan salah, coba lagi!")

st.write("Tebak angka antara 1 sampai 50.")

# Menggunakan layout kolom

import streamlit as st 

st.title("Buat ngitung pengeluaran anak kucai") 


col1, col2 = st.columns(2)

with col1:
    st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
    angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

    if (angka % 2) == 0:
        st.write(f"{angka} adalah Bilangan Genap")
    else:
        st.write(f"{angka} adalah Bilangan Ganjil")

with col2:
    st.header("Aplikasi menghitung Total Gambling")

    def hitung_total(harga, jumlah):
        return harga * jumlah

    harga_barang = st.number_input("Masukkan Harga Barang:", value=0, step=1000)
    jumlah_barang = st.number_input("Masukkan Jumlah Barang:", value=0, step=1)
    total_harga = hitung_total(harga_barang, jumlah_barang)

    if total_harga > 100000:
        total_harga_diskon = total_harga - 0.05 * total_harga
        st.write(f"Total Harga (dengan diskon): Rp. {total_harga_diskon:,.0f}")
    else:
        st.write(f"Total Harga: Rp. {total_harga:,.0f}")

    bayar = st.number_input("Masukkan Jumlah Uang:", value=0, step=10000)

    if bayar >= total_harga:
        kembalian_uang = bayar - total_harga
        st.write(f"Uang Kembalian: Rp. {kembalian_uang:,.0f}")
    else:
        st.write("Uang yang anda bayarkan kurang ")
