import streamlit as st
import streamlit.components.v1 as components

st.title("webpage accessed")

# components.iframe("https://py-slack.virajkhatavkar.com", width=800, height=600)
components.iframe("https://www.tickertape.in/market-mood-index", width=1000, height=1000, scrolling=True)
