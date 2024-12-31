# cek_keuangan.py

import streamlit as st

def format_rupiah(angka):
    """Format angka ke dalam format rupiah tanpa simbol."""
    return f"{angka:,.0f}".replace(',', '.')

def cek_keuangan_page():
    st.title("Cek Keuangan")


    daftar_pemasukan = st.session_state.get('Daftar_Pemasukan', [])
    daftar_pengeluaran = st.session_state.get('Daftar_Pengeluaran', [])
    total_pemasukan = sum(int(item['Jumlah'].replace('.', '').replace(',', '')) for item in daftar_pemasukan)
    total_pengeluaran = sum(int(item['Jumlah'].replace('.', '').replace(',', '')) for item in daftar_pengeluaran)
    
    saldo = total_pemasukan - total_pengeluaran


    st.subheader("Ringkasan Keuangan")
    st.write(f"Total Pemasukan: Rp.{format_rupiah(total_pemasukan)}")
    st.write(f"Total Pengeluaran:  Rp.{format_rupiah(total_pengeluaran)}")
    st.write(f"Saldo Saat Ini: Rp.{format_rupiah(saldo)}")

    if daftar_pemasukan:
        st.subheader("Daftar Pemasukan")
        for item in daftar_pemasukan:
            st.write(f"{item['Tanggal']} - {item['Sumber']}: Rp.{item['Jumlah']}")

    if daftar_pengeluaran:
        st.subheader("Daftar Pengeluaran")
        for item in daftar_pengeluaran:
            st.write(f"{item['Tanggal']} - {item['Sumber']}: Rp.{item['Jumlah']}")
            
    
            
