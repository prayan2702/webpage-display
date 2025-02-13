import streamlit as st
import streamlit.components.v1 as components

st.title("webpage accessed")

# components.iframe("https://py-slack.virajkhatavkar.com", width=800, height=600)
# CSS कोड जोड़ें
st.markdown(
    """
    <style>
    iframe {
        width: 100vw;
        height: 100vh;
        position: fixed;
        top: 0;
        left: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(
    """
    <iframe src="https://www.portfolioyoga.com/wp/"></iframe>
    """,
    height=0,
    width=0
)
