import streamlit as st
from datetime import datetime

class Pengeluaran:
    def __init__(self, sumber, jumlah, tanggal):
        self.sumber = sumber  
        self.jumlah = jumlah  
        self.tanggal = tanggal  

    def format_jumlah(self):
        """Format jumlah ke dalam format rupiah tanpa simbol."""
        return f"{self.jumlah:,.0f}".replace(',', '.')

def pengeluaran_page():
    st.title("Pencatatan Pengeluaran")


    with st.form(key='pengeluaran_form'):
        sumber_pengeluaran = st.text_input("Sumber Pengeluaran:")
        jumlah_pengeluaran = st.text_input("Jumlah Pengeluaran (Rp):")
        tanggal_pengeluaran = st.date_input("Tanggal Pengeluaran:", datetime.now())
        submit_button = st.form_submit_button(label='Tambahkan')

    if submit_button:
        if jumlah_pengeluaran.strip() == "":
            st.error("Jumlah pengeluaran tidak boleh kosong!")
        else:
            pengeluaran_entry = Pengeluaran(
                sumber=sumber_pengeluaran,
                jumlah=int(jumlah_pengeluaran.replace('.', '').replace(',', '')),
                tanggal=tanggal_pengeluaran
            )
            
            if 'Daftar_Pengeluaran' not in st.session_state:
                st.session_state['Daftar_Pengeluaran'] = []
                
            st.session_state['Daftar_Pengeluaran'].append({
                'Jumlah': pengeluaran_entry.format_jumlah(),  
                'Tanggal': pengeluaran_entry.tanggal,          
                'Sumber': pengeluaran_entry.sumber             
            })
            st.success("Pengeluaran berhasil ditambahkan!")
    else:
        st.info("Silakan masukkan data pengeluaran untuk menambahkannya.")

if __name__ == "__main__":
    pengeluaran_page()