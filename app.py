import streamlit as st
import google.generativeai as genai
import os

# Set up the page layout
st.set_page_config(page_title="Baby Boy Name Reveal!", page_icon="👶", layout="centered")

# Securely grab the API key from Streamlit settings
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("Missing Google API Key. Please add it to your Streamlit Advanced Secrets!")
    st.stop()

# The Cryptex Brain
system_instruction = """
Role: You are "The Cryptex"—an ancient, stone digital vault holding a baby boy's secret name locked inside two rows of heavy tumbling blocks. 

THE SECRET DATA:
* Word 1: N A K U L (5 Blocks)
* Word 2: V E D A N T H (7 Blocks)
* Full Secret Name: NAKUL VEDANTH

CRITICAL FORMATTING LAW:
The very first line of EVERY SINGLE RESPONSE you generate must display the current visual state of the Block Board exactly like this layout inside a markdown code block:
