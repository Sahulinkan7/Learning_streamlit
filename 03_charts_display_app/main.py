import streamlit as st
import pandas as pd
import os
st.set_page_config(page_title="chart display")

df = pd.read_csv("data/sample_map.csv")
st.map(df)

df2=pd.read_csv("data/sample.csv")

st.line_chart(df2,x='year',y=['col1','col2','col3'])

