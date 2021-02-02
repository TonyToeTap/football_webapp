# link: https://www.youtube.com/watch?v=-IM3531b1XU
# YT-tutorial:

import streamlit as st
import pandas as pd
import numpy as np
from sodapy import Socrata


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()


st.markdown(
    """
    <style>
    .main {
    background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)


with header:
    st.title('Football Analytics App')
    st.text('In this project I try to improve my Python-Skills by playing around with NFL data')

with dataset:
    st.header('')
    st.text('')











