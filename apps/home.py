import pandas as pd
import streamlit as st
from PIL import Image

def app():
    st.title("Home")
    st.write('Halaman ini berisikan informasi umum dari aplikasi web Final Grades Predictor')

    image = Image.open('logo.png')

    st.image(image)

    st.header("Tentang FGP")
    st.write("""
    #### Nama Aplikasi
    Machine Learning - Final Grades Predictor

    #### Fungsi Utama
    Aplikasi ini mempunyai fungsi utama yaitu memprediksi hasil akhir siswa pada suatu pelajaran berdasarkan dari tingkat kehadiran dan nilai akhir mata pelajaran dengan menggunakan metode Machine Learning.
    
    #### Fitur-Fitur
    1. Home - berisikan informasi umum mengenai aplikasi web FGP
    2. Exploratory Data Analysis - berisikan informasi umum dari data yang digunakan sebagai sample aplikasi web FGP
    3. Model - model machine learning yang dikembangkan untuk fungsi utama aplikasi web FGP

    #### Manfaat Secara Umum
    Aplikasi Web FGP ini apabila diintegrasikan dengan LMS atau sekolah yang mempunyai rekap nilai online seperti Goolge Classroom, bisa memberikan early warning kepada siswa yang dianggap sistem mempunyai potensi untuk tidak memenuhi standar kelulusan minimal pada suatu pelajaran berdasarkan kriteria atau parameter yang sudah ditentukan sebelumnya, sehingga guru bisa memberikan arahan kepada siswa untuk melakukan perbaikan pada aspek yang perlu dibenahi.

    #### Sumber Data dan Tipe Data
    Dataset yang digunakan pada aplikasi ini diperoleh dari pustaka data SMA Global Islamic Boarding School untuk kategori hasil akhir siswa kelas 10 dan 11 semester ganjil dan genap
    """)

    df = pd.read_csv('full_year.csv')
    st.write(df.head(5))
    st.write(df.tail(5))

    st.write("""
    #### Fitur Yang Bisa Dikembangkan
    1. Fitur upload dataset
    2. FItur EDA yang lebih dinamis dan interaktif
    3. Cleaning dataset untuk hasil model yang lebih maksimal
    4. Tuning parameter yang cocok untuk hasil model yang lebih maksimal


    #### Pengembang
    Muhammad Amin, Guru SMA Global Islamic Boarding School, Alalak, Kalimantan Selatan
    """)