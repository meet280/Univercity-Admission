import streamlit as st
import pandas as pd
import numpy as np
import pickle

clf=pickle.load(open("case_study_university.pkl","rb"))

def predict(data):
    clf=pickle.load(open("case_study_university.pkl","rb"))
    return clf.predict(data)

st.title("Advertising Spends Prediction using Machine Learning")
st.markdown("This Model Identify total spend")

st.header("Media Advertising Spends")
col1,col2 = st.columns(2)

with col1:
	st.text("TV")
	TV = st.slider("Advertising on TV", 1.0, 10000.0, 0.5)
	st.text("Radio")
	RD = st.slider("Advertising on Radio", 1.0, 10000.0, 0.5)
	st.text("Newspaper")
	NP= st.slider("Advertising on Newspaper", 1.0,10000.0,0.5)


st.text('')
if st.button("Predict Total Sales Price on Media "):
    result = predict(
        np.array([[TV,RD,NP]]))
    st.text(result[0])
