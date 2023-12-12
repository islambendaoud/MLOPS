import streamlit as st 
import requests
import os 
import pandas as pd

url = os.getenv("URL")


tab1, tab2 = st.tabs(["Analyze", "History"])

with tab1:
    s = st.text_input("To analyze", "Type here ...")
    b= st.button("Submit")
    if b:
        url_1 = url + "/predict"
        body = {
            "reviews" : [s]
        }
        reponse = requests.post(url_1 , json=body)
        sentiment = reponse.json()['predictions'][0]

        st.write("You entered: ", s)
        st.write('Sentiments is : ' , sentiment)

with tab2:
    url_2 = url + "/history"
    reponse = requests.post(url_2).json()

    history = pd.json_normalize(reponse)
    # drop the _id
    history = history.drop(columns="_id")

    st.table(history)
