# app.py

import streamlit as st
from dashboard import dashboard_page
from pemasukan import pemasukan_page
from pengeluaran import pengeluaran_page
from cek_keuangan import cek_keuangan_page
from tabungan import tabungan_page


if 'Daftar_Pemasukan' not in st.session_state:
    st.session_state['Daftar_Pemasukan'] = []
if 'Daftar_Pengeluaran' not in st.session_state:
    st.session_state['Daftar_Pengeluaran'] = []
if 'Daftar_Tabungan' not in st.session_state:
    st.session_state['Daftar_Tabungan'] = []


st.sidebar.title("Smart Finance")
page_options = {
    "Dashboard": dashboard_page,
    "Pemasukan": pemasukan_page,
    "Pengeluaran": pengeluaran_page,
    "Cek Keuangan": cek_keuangan_page,
    "Tabungan": tabungan_page,
}

selected_page = st.sidebar.selectbox("Pilih Halaman", list(page_options.keys()))
page_options[selected_page]()  