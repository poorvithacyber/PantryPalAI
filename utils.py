import streamlit as st

def show_error(message: str):
    st.error(f"Error: {message}")

def show_success(message: str):
    st.success(message)

def show_warning(message: str):
    st.warning(message)
