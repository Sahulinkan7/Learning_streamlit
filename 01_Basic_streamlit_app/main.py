import streamlit as st

st.title("This is the Title of this page")


st.header("Heading of this page")
st.subheader("This is the sub header of this page")

st.text("Hello this is plain text")

st.markdown("This is markdown **Text**")
st.markdown("# Header1")
st.markdown("## Header2")
st.markdown("### Header3")
st.markdown("[click here]()")
st.caption("This is a caption")

st.code("import streamlit as st",language="python")
st.code("print('Hello streamlit')",language="python")

st.code("""import pandas as pd
df=pd.read_csv(myfilepath)""")

st.text("no format text")

st.latex("f(x)=2*x^2")

st.text("text above divider")
st.divider()
st.text("text below divider")

st.write("st write text")