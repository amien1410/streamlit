import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from sklearn import preprocessing

def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("EDA - Exploratory Data Analysis")
    st.write('Di halaman ini kita bisa melihat grafik perbandingan jumlah siswa yang lulus dan recourse pada setiap mata pelajaran dari kelas dan semester tertentu')

    df = pd.read_csv('full_year.csv')

    label_encoder = preprocessing.LabelEncoder()
    df['status'] = label_encoder.fit_transform(df['hasil_akhir'])

    # total siswa per mapel
    mapel = df.groupby(['semester', 'kelas', 'mapel'])['hasil_akhir'].count().reset_index()
    mapel.rename(columns = {'hasil_akhir':'total_siswa'}, inplace = True)

    # total siswa lulus per mapel
    lulus = df[df.hasil_akhir == 'lulus'].groupby(['semester', 'kelas', 'mapel'])['status'].count().reset_index()
    lulus.rename(columns = {'status':'total_lulus'}, inplace = True)

    # konversi total siswa dan lulus ke percentage
    lulus['percentage'] = [i / j * 100 for i,j in zip(lulus['total_lulus'], mapel['total_siswa'])]
    mapel['percentage'] = [i / j * 100 for i,j in zip(mapel['total_siswa'], mapel['total_siswa'])]

    kelas = st.sidebar.selectbox("Pilih Kelas", (10, 11))
    semester = st.sidebar.selectbox("Pilih Semester", ("ganjil", "genap"))

    if kelas == 11:
        if semester == 'genap':
            ks_total = mapel.loc[(mapel.kelas == 11) & (mapel.semester == 'genap'), ['mapel', 'percentage']]
            ks_lulus = lulus.loc[(lulus.kelas == 11) & (lulus.semester == 'genap'), ['mapel', 'percentage']]
            judul_barplot = 'Persentase Lulus dan Recourse Kelas 11 Semester Genap'
        else:
            ks_total = mapel.loc[(mapel.kelas == 11) & (mapel.semester == 'ganjil'), ['mapel', 'percentage']]
            ks_lulus = lulus.loc[(lulus.kelas == 11) & (lulus.semester == 'ganjil'), ['mapel', 'percentage']]
            judul_barplot = 'Persentase Lulus dan Recourse Kelas 11 Semester Ganjil'
    else:
        if semester == 'genap':
            ks_total = mapel.loc[(mapel.kelas == 10) & (mapel.semester == 'genap'), ['mapel', 'percentage']]
            ks_lulus = lulus.loc[(lulus.kelas == 10) & (lulus.semester == 'genap'), ['mapel', 'percentage']]
            judul_barplot = 'Persentase Lulus dan Recourse Kelas 10 Semester Genap'
        else:
            ks_total = mapel.loc[(mapel.kelas == 10) & (mapel.semester == 'ganjil'), ['mapel', 'percentage']]
            ks_lulus = lulus.loc[(lulus.kelas == 10) & (lulus.semester == 'ganjil'), ['mapel', 'percentage']]
            judul_barplot = 'Persentase Lulus dan Recourse Kelas 10 Semester Ganjil'

    # st.dataframe(ks_lulus)

    font1 = {'family':'serif','color':'blue','size':20}
    font2 = {'family':'serif','color':'darkred','size':15}

    # setting sns barplot
    sns.set(rc={"figure.figsize":(16, 10)})
    plt.xticks(rotation=45)

    # barplot bertindih, bar1 = total siswa, bar2 = total lulus
    bar1 = sns.barplot(x="mapel",  y="percentage", data=ks_total, color='#a6bddb')
    bar2 = sns.barplot(x="mapel", y="percentage", data=ks_lulus, color='#1c9099')

    # menambahkan legend di barplot
    top_bar = mpatches.Patch(color='#a6bddb', label='Recourse')
    bottom_bar = mpatches.Patch(color='#1c9099', label='Lulus')
    plt.legend(handles=[top_bar, bottom_bar])
    plt.title(judul_barplot, fontdict = font1)
    plt.xlabel("Mapel", fontdict = font2)
    plt.ylabel("Persentase", fontdict = font2)

    st.pyplot()