import pandas as pd
import numpy as np
import pickle
import streamlit as st

classifier=pickle.load(open("classifier.pkl","rb"))

def predict_note_authentication(variance,skewness,curtosis,entropy):
                                prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
                                print(prediction)
                                return prediction
                    
def main():
    st.title("Bank Authenticator")
    html_temp="""
    <div style="background-color:orange;padding:10px">
    <h2 style='color:white;textt_align:center;">Streamlit Bank Authenticator App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance=st.text_input("Variance","Enter Here")
    skewness=st.text_input("Skewness","Enter Here")
    curtosis=st.text_input("Curtosis","Enter Here")
    entropy=st.text_input("Entropy","Enter Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("This app is built using Strealit")

    
if __name__=='__main__':
    main()
