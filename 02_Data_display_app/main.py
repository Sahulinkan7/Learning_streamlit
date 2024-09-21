import streamlit as st
import pandas as pd 

st.set_page_config(page_title="data display",layout="wide")


data={"name":["Linkan Sahu","abc","amit"],
      "email":["sahulinkan7@gmail.com","abc@rtr.com","amit@hh.com"]}

df=pd.DataFrame(data)

st.title("Data Display in Streamlit")

st.subheader("showing dataframe in streamlit")
st.dataframe(df)

st.metric(label="population",value=1200,delta=30,delta_color="normal")

st.subheader("showing data using write")
st.write(df)

st.subheader("showing dataframe as table")
st.table(df)

