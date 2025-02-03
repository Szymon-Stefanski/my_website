import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(".venv/Images/profil.jpg")

with col2:
    st.title("Szymon Stefański")
    content = """
    I'm Szymon, a 3rd-year Computer Science student at the Polish-Japanese Academy of Information Technology. 
    I love learning new technologies and applying them to real-world problems.
    """
    st.info(content)