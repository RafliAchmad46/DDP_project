# dashboard.py

import streamlit as st
import pandas as pd

st.title("SmartFinance")

def dashboard_page():
    st.title("Dashboard Keuangan")

    if 'Daftar_Pemasukan' not in st.session_state:
        st.session_state['Daftar_Pemasukan'] = []
    if 'Daftar_Pengeluaran' not in st.session_state:
        st.session_state['Daftar_Pengeluaran'] = []
    if 'Daftar_Tabungan' not in st.session_state:
        st.session_state['Daftar_Tabungan'] = []


    data_dict = {
        "Daftar Pemasukan": st.session_state['Daftar_Pemasukan'],
        "Daftar Pengeluaran": st.session_state['Daftar_Pengeluaran'],
        "Daftar Tabungan": st.session_state['Daftar_Tabungan']
    }

    for title, data in data_dict.items():
        st.subheader(title)
        if data:
            df = pd.DataFrame(data)
            df.reset_index(drop=True, inplace=True)  
            df.index += 1  
            st.dataframe(df)
        else:
            st.write(f"Belum ada data {title.lower()}.")


if __name__ == "__main__":
    dashboard_page()
