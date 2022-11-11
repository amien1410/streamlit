import streamlit as st
from PIL import Image

class MultiApp:
    def __init__(self):
        self.apps = []
    
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    
    def run(self):
        image = Image.open('logo-mini.png')
        app = st.sidebar.image(image)
        app = st.sidebar.selectbox(
            'MENU',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()