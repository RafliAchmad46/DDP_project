# tabungan.py

import streamlit as st
from datetime import datetime

def format_rupiah(angka):
    """Format angka ke dalam format rupiah tanpa simbol."""
    return f"{angka:,.0f}".replace(',', '.')

def tabungan_page():
    st.title("Pencatatan Tabungan")

    
    if 'Daftar_Tabungan' not in st.session_state:
        st.session_state['Daftar_Tabungan'] = []

   
    with st.form(key='tabungan_form'):
        tujuan_tabungan = st.text_input("Tujuan Menabung:")
        jumlah_tabungan = st.text_input("Jumlah Tabungan (Rp):")
        tanggal_tabungan = st.date_input("Tanggal Tabungan:", datetime.now())
        
      
        target_tabungan = st.text_input("Target Tabungan (Rp):")
        jangka_waktu = st.number_input("Jangka Waktu (bulan):", min_value=1, step=1)

        submit_button = st.form_submit_button(label='Tambahkan')

        if submit_button:
            if not tujuan_tabungan or not jumlah_tabungan or not target_tabungan:
                st.warning("Semua kolom harus diisi sebelum menambahkan tabungan!")
            else:
                formatted_jumlah = format_rupiah(int(jumlah_tabungan.replace('.', '').replace(',', '')))
                formatted_target = format_rupiah(int(target_tabungan.replace('.', '').replace(',', '')))
            
                st.session_state['Daftar_Tabungan'].append({
                    'Jumlah': formatted_jumlah,
                    'Tanggal': tanggal_tabungan,
                    'Tujuan': tujuan_tabungan,
                    'Target': formatted_target,
                    'Jangka Waktu': jangka_waktu
                })
                st.success("Tabungan berhasil ditambahkan!")

                if target_tabungan:
                    target_numeric = int(target_tabungan.replace('.', '').replace(',', ''))
                    monthly_savings_needed = target_numeric / jangka_waktu
                    st.write(f"Untuk mencapai target tabungan Rp {formatted_target} dalam {jangka_waktu} bulan, Anda perlu menabung sekitar Rp {format_rupiah(monthly_savings_needed)} per bulan.")

if __name__ == "__main__":
    tabungan_page()  