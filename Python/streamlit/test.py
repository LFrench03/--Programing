import streamlit as st
import pandas as pd
#Text Widgets
st.title("Hello there! I am a Streamlit Web App",anchor="Title")
st.subheader("Hi! I am your Subheader", divider="blue")
st.header("I am Header")
st.text("Hi there, i am a text function and programmers uses me inplace of paragrapghs")
st.markdown("[Google](https://www.google.com)")
st.markdown("----")
st.caption("This is a caption")
st.latex(r"LaTeX~Matrix\begin{pmatrix}a&b\\c&d\end{pmatrix}")
json = {"json": "data structure"}
st.json(json)
code = '''import streamlit as st'''
st.code(code,language="python")
st.write("## H2")
st.metric(label = "Wind Speed", value = "120ms⁻¹", delta ="-11.4ms⁻¹")
dataframe = pd.DataFrame({"Column 1" :[1,2,3], "Column 2" : [4,5,6]},index=["I","II","III"])
st.table(dataframe)
st.caption("This is a streamlit table")
st.dataframe(dataframe ,width=500, height=245)
st.caption("And this is a streamlit dataframe")
#Media Widgets
st.image("Python/streamlit/img/streamlit_logo.png",width=600)
st.audio("Python/streamlit/audio/testaudio.mp3")
st.video("Python/streamlit/video/testvideo.mp4")
#Interactive Widgets
def change():
    print(st.session_state.checker)
state = st.checkbox("Checkbox", value=True, on_change=change, key="checker")
