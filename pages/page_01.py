import streamlit as st

st.write("Let's get our secrets!")

spell = st.secrets['spell']
key = st.secrets.some_magic_api.key

st.write(f"Our secret spell is : {spell}")

st.write(f"Our secret key is : {key}")