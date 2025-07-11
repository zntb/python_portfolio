import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)
    
    with col2:
        st.title("John Doe")
        content = """
Tempor pariatur cupidatat labore consectetur eu consectetur reprehenderit reprehenderit dolor aliquip ut excepteur. Labore ex eiusmod pariatur excepteur fugiat qui aliqua non eiusmod et consectetur eu. Amet incididunt nostrud labore commodo mollit adipisicing exercitation. Et est eiusmod quis reprehenderit occaecat consectetur incididunt nulla velit. Veniam occaecat velit magna mollit elit laboris labore consequat.
Dolore dolore exercitation anim cupidatat laborum tempor cillum ea exercitation consectetur. Ipsum minim magna officia aliquip consequat aliqua ullamco laboris aliqua. Ad mollit sunt ullamco ad duis enim laborum qui esse consequat labore sint eu.
Incididunt sunt labore ut nulla fugiat qui ad qui amet laboris ut pariatur. Amet aliquip ex sunt sint irure. Proident deserunt ad esse deserunt consequat eu est officia nisi quis elit non do.
Officia duis reprehenderit aliqua laboris. Sunt sint et mollit enim id. Cillum consectetur fugiat nulla nulla reprehenderit Lorem enim. Deserunt elit cillum nulla aliqua enim proident et laboris. Adipisicing occaecat cillum sint ea ea sit. Est ad Lorem dolor eiusmod excepteur voluptate incididunt adipisicing. Nostrud dolore laborum sunt Lorem.
Ea duis in excepteur pariatur amet quis cupidatat velit. Eu proident consequat deserunt dolor ea. Eiusmod laboris cupidatat duis ea consectetur reprehenderit nisi incididunt eu exercitation et exercitation ad. Irure consequat mollit nostrud dolore anim anim pariatur. Aliqua minim duis voluptate aliquip id ut dolor anim amet nostrud labore excepteur. Voluptate sit proident velit cupidatat cillum.
Mollit proident esse deserunt voluptate non aute velit adipisicing voluptate ex sunt. Laborum nostrud irure cupidatat est magna. Est reprehenderit laboris eu dolore occaecat eu duis. Officia labore eiusmod reprehenderit id.
        """
        st.info(content)
        
        
st.write("---")

content2 = """
Elit elit proident consectetur duis ea adipisicing dolore aliqua pariatur pariatur magna sit.
"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
  for index, row in df[:10].iterrows():
          st.header(row["title"])
          st.write(row["description"])
          st.image("images/" + row["image"])
          st.write(f"[Source Code]({row['url']})")
          
with col4:
  for index, row in df[10:].iterrows():
          st.header(row["title"])
          st.write(row["description"])
          st.image("images/" + row["image"])
          st.write(f"[Source Code]({row['url']})")