import streamlit as st
import nlpcloud

st.set_page_config(layout='wide')
st.title("Получи препоръка за своето мотивационно писмо", anchor=None)

text = st.text_area('Mотивационно писмо')
button = st.button('Прати')

if button:
    client = nlpcloud.Client('gpt-j', "a2a44e51e1e17b4f7685ab7509fc323b3834aa50", True, 'bg')
    response = client.gs_correction(text)
    st.header('Препоръка:')
    st.write(response['correction'])