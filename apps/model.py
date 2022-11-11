# import modules utama
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# import modules algoritma
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA

def app():
    st.title("Final Grades Predictor - ML Model")
    st.write('FGP menyediakan beberapa algoritma pilihan untuk digunakan sebagai Classifier dalam memprediksi hasil akhis siswa berdasarkan data yang sudah disiapkan beserta dengan Parameter Algoritma yang berfungsi untuk mencapai hasil akurasi yang maksimal dari algoritma yang dipilih')

    classifier = st.sidebar.selectbox("ALGORITMA", ("KNN", "SVM", "Random Forest", "Decision Tree"))

    X, y = get_dataset()
    # st.write("Ukuran dataset : ", X.shape)

    params = get_classifier_params(classifier)

    clf = get_classifier(classifier, params)

    # classification
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1234)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    st.write(f"Nama Algoritma : {classifier}")

    st.write(f"Tingkat Akurasi : {acc}")

    d = {'Actual': y_test, 'Prediction': y_pred}
    comparation = pd.DataFrame(data = d)
    st.dataframe(comparation)



def get_dataset():
    data = pd.read_csv("full_year.csv")
    X = data[['kehadiran', 'nilai_mapel']]
    y = data['hasil_akhir']
    return X, y

def get_classifier_params(classifier):
    params = dict()
    if classifier == "KNN":
        K = st.sidebar.slider("K", 1, 15)
        params["K"] = K
    elif classifier == "SVM":
        C = st.sidebar.slider("C", 0.01, 10.0)
        params["C"] = C
    elif classifier == "Random Forest":
        max_depth = st.sidebar.slider("max_depth", 2, 15)
        n_estimators = st.sidebar.slider("n_estimators", 1, 100)
        random_state = st.sidebar.slider("random_state", 1, 100)
        params['max_depth'] = max_depth
        params["random_state"] = random_state
        params['n_estimators'] = n_estimators
    else:
        criterion = st.sidebar.selectbox("Pilih Kriteria", ("gini", "entropy"))
        max_depth = st.sidebar.slider("max_depth", 1, 15)
        random_state = st.sidebar.slider("random_state", 1, 100)
        min_samples_leaf = st.sidebar.slider("min_samples_leaf", 1, 15)
        params["criterion"] = criterion
        params["max_depth"] = max_depth
        params["random_state"] = random_state
        params["min_samples_leaf"] = min_samples_leaf
    return params

def get_classifier(classifier, params):
    if classifier == "KNN":
        clf = KNeighborsClassifier(n_neighbors = params["K"])
    elif classifier == "SVM":
        clf = SVC(C = params["C"])
    elif classifier == "Random Forest":
        clf = RandomForestClassifier(
            n_estimators = params["n_estimators"],
            max_depth = params["max_depth"],
            random_state = params["random_state"]
        )
    else:
        clf = DecisionTreeClassifier(
            criterion = params["criterion"],
            min_samples_leaf= params["min_samples_leaf"],
            max_depth = params["max_depth"],
            random_state = params["random_state"]
        )
    return clf