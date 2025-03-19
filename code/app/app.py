import streamlit as st
import requests

st.title("Запрос к другому контейнеру")
st.text("s-строка, n-число раз, которое строка повторится")
s = st.text_input("s")
n = st.number_input("n", min_value=1, step=1)

button = st.button("Отправить запрос")

if button:
    if not s:
        st.error("Поле 's' обязательно для заполнения.")
    if not n:
        st.error("Поле 'n' обязательно для заполнения.")
    
    data = {
        "string": str(s), 
        "num" : int(n)
            }
    try:
        response = requests.post("http://api:8000/sample_endpoint", json=data)
        
        if response.status_code == 200:
            st.success(f"Ваша измененная строка: {response.json()}")
        else:
            st.error(f"Ошибка: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Ошибка при отправке запроса: {e}")
