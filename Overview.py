import streamlit as st
from langfuse import Langfuse

"""
# Langfuse Playground
"""
# https://langfuse.com/docs/sdk/python/low-level-sdk#debug-mode
# BUG: Currently would have 502 error
langfuse = Langfuse(debug=True)
st.write(langfuse.auth_check())
