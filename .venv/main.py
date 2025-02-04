import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image(".venv/Images/profil.jpg")

with col2:
    st.title("Szymon Stefański")
    content = """
    I'm Szymon, a 3rd-year Computer Science student at the Polish-Japanese Academy of Information Technology. 
    I love learning new technologies and applying them to real-world problems.\n
    📚 What I’m learning:\n
    I'm focusing on enhancing my skills in:
    
    Learning Python and Bash, particularly for automation tasks such as streamlining workflows, managing files, 
    and creating utility scripts.\n
    Database management and optimization with Oracle SQL and PL/SQL.\n
    Frontend development using HTML, CSS, and JavaScript.\n
    Exploring Arduino for hobby projects and understanding hardware-software integration.\n
    """
    st.info(content)

st.write("Example text to show")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv(".venv/data.csv", sep=";")

with col3:
    for index, row in df[:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(".venv/Images/" + row["image"])
        st.write(f"[Github repository]({row['url']})")

with col4:
    for index, row in df[1:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        #st.image(".venv/Images/" + row["image"])
        st.write(f"[Github repository]({row['url']})")