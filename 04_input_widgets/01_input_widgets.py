import streamlit as st 
import pandas as pd 

st.divider()

colm1,colm2=st.columns([0.6,0.4])
colm1.write("first col")
## select box
select=colm1.selectbox(label="select column",options=['col1','col2','col3'])

if select:
    colm2.write(select)
    colm2.text(f"showing coloumn data for column {select}")
    df=pd.read_csv("./data/sample.csv")
    colm2.dataframe(df[select],hide_index=True)
    print(df[select])
    
st.divider()