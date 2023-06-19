import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")

content = """
Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan.
"""
st.write(content)

st.subheader("Our Team")

col1, col2, col3, = st.columns(3)

df = pandas.read_csv("files/data.csv")


with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("files/images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("files/images/" + row['image'])


with col3:
    for index, row in df[8:].iterrows():
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.write(row["role"])
        st.image("files/images/" + row['image'])


