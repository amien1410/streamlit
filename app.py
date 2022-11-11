# import modules yang diperlukan
import streamlit as st
from multiapp import MultiApp
from apps import home, eda, model

# load judul dan icon web app
st.set_page_config(
    page_title = 'Final Grades Predictor',
    page_icon = '🏆'
)
# load modul multiapp
app = MultiApp()

# load semua aplikasi bawaan di sini
app.add_app("Home", home.app)
app.add_app("Exploratory Data Analysis", eda.app)
app.add_app("Final Grades Predictor - ML Model", model.app)

# jalankan aplikasi utama di sini
app.run()