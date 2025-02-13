import streamlit as st
import streamlit.components.v1 as components

st.title("webpage accessed")

components.iframe("https://www.google.com", width=800, height=600)
