import streamlit as st

st.set_page_config(page_title="Test Website", page_icon=":tada:", layout= "wide")

#----HEADER SECTION----
with st.container():
    st.title ("Hi, I am Utochukwu :wave:")
    st.write ("I am a 15 year old in Estonia and i am into programming with languages such as Python")
    st.write ("I use Python to write basic programs and i am still learning how to use it effectively in all settings")
    st.write('[learn more](https://pythonandvba.com)')
#-------WHAT I DO--------
with st.container():
    st.subheader("PLEASE NOTE THAT THIS IS A TEST VERSION AND DO NOT SHARE THE LINK WITH ANYONE ELSE WITHOUT AUTHORIZATION!!!!")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("All about me")
        