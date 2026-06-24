import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="👶 Name Reveal!", layout="centered", page_icon="✨")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container { padding-top: 0.2rem; padding-bottom: 0rem; }
    </style>
""", unsafe_allow_html=True)

# Python simply reads the game.html file off the hard drive and displays it
with open("game.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=840)
