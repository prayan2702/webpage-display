import streamlit as st
import streamlit.components.v1 as components

st.title("webpage accessed")

# components.iframe("https://py-slack.virajkhatavkar.com", width=800, height=600)
components.iframe("https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%20IT", width=1000, height=1000, scrolling=True)
