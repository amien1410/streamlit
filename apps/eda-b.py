import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn import preprocessing

def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title("EDA - Exploratory Data Analysis")
    st.write('This is data page')

    df = pd.read_csv('data.csv')
    # st.dataframe(df)

    label_encoder = preprocessing.LabelEncoder()
    df['status'] = label_encoder.fit_transform(df['hasil_akhir'])

    mapel = df.groupby(['mapel', 'hasil_akhir'])['status'].count().reset_index()
    mapel.rename(columns = {'status':'total_siswa'}, inplace = True)

    # sns.set_theme(style="whitegrid")
    sns.set(rc={"figure.figsize":(16, 10)})
    plt.xticks(rotation=45)

    sns.barplot(x="mapel", y="total_siswa", hue='hasil_akhir', data=mapel)
    st.pyplot()

    