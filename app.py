import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Diagnostic Radar", layout="centered")

st.title("🔍 Engine Diagnostic Mode")

if "GOOGLE_API_KEY" not in st.secrets:
    st.error("🚨 CRITICAL: Streamlit cannot find a secret named 'GOOGLE_API_KEY'.")
    st.stop()

api_key = st.secrets["GOOGLE_API_KEY"]

st.write("### 1. API Key Health Check")
st.write(f"- **First 6 characters:** `{api_key[:6]}`")
st.write(f"- **Total character count:** `{len(api_key)}` *(A standard Google Key is exactly 39 characters)*")

st.write("---")
st.write("### 2. Pinging Google's Mainframe...")

try:
    genai.configure(api_key=api_key)
    
    # Ask Google to hand over the list of every model this key is allowed to touch
    available_models = [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
    
    st.success("🟢 SUCCESS! The Key is valid and talking to Google.")
    st.write("#### Here is the exact list of models your account is authorized to use:")
    st.json(available_models)

except Exception as e:
    st.error("🔴 FAILED TO CONNECT TO GOOGLE SERVER.")
    st.code(str(e))
