import streamlit as st
from datetime import datetime

class Pemasukan:
    def __init__(self, sumber, jumlah, tanggal):
        self.sumber = sumber   
        self.jumlah = jumlah  
        self.tanggal = tanggal  

    def format_jumlah(self):
        """Format jumlah ke dalam format rupiah tanpa simbol."""
        return f"{self.jumlah:,.0f}".replace(',', '.')

def pemasukan_page():
    st.title("Pencatatan Pemasukan")


    with st.form(key='pemasukan_form'):
        sumber_pemasukan = st.text_input("Sumber Pemasukan:")
        jumlah_pemasukan = st.text_input("Jumlah Pemasukan (Rp):")
        tanggal_pemasukan = st.date_input("Tanggal Pemasukan:", datetime.now())
        submit_button = st.form_submit_button(label='Tambahkan')

    if submit_button:
        if jumlah_pemasukan.strip() == "":
            st.error("Jumlah pemasukan tidak boleh kosong!")
        else:
            pemasukan_entry = Pemasukan(
                sumber=sumber_pemasukan,
                jumlah=int(jumlah_pemasukan.replace('.', '').replace(',', '')),
                tanggal=tanggal_pemasukan
            )
            
            if 'Daftar_Pemasukan' not in st.session_state:
                st.session_state['Daftar_Pemasukan'] = []
                
            st.session_state['Daftar_Pemasukan'].append({
                'Jumlah': pemasukan_entry.format_jumlah(),  
                'Tanggal': pemasukan_entry.tanggal,         
                'Sumber': pemasukan_entry.sumber              
            })
            st.success("Pemasukan berhasil ditambahkan!")
    else:
        st.info("Silakan masukkan data pemasukan untuk menambahkannya.")

if __name__ == "__main__":
    pemasukan_page()