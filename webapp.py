import streamlit as st
from altair.vegalite.v4.schema.core import Align
import numpy as np
import pandas as pd
import os
import base64
import streamlit.components.v1 as components
import pickle
import zipfile
import tempfile
import requests

st.set_page_config(layout="wide")

def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
def set_png_as_page_bg(png_file):
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)
        return
set_png_as_page_bg('Static/homef.gif')

a,b,c=st.beta_columns(3)
b.image('Static/logo.jpeg')

html_temp1 = """
    
    <h3 style="color:red;text-align:center;"> Worried about you package delivery date ?</h3>
    </div>
    """
st.markdown(html_temp1, unsafe_allow_html = True)
html_temp = """
    
    <h3 style="color:black;text-align:center;"> Dont Stress We got you covered. Enter basic package details and TADAHH you can find out if it's reaching on time or not</h3>
    </div>
    """
st.markdown(html_temp, unsafe_allow_html = True)

html_temp2 = """
    <h1 style="color:black;text-align:center;"> FIND OUT NOW!!!</h1>
    </div>
    """
st.markdown(html_temp2, unsafe_allow_html = True)


with open("delivery.pkl", "rb") as f:
    data = pickle.load(f)

def main():
    import streamlit as st
    a,b,c=st.beta_columns(3)
    display = ("Flight", "Ship","Road")
    options = list(range(len(display)))
    f1 = b.selectbox("Mode of Shipment", options, format_func=lambda x: display[x])
    b.write(f1)
    f2= b.slider("Number of calls from company",0,10)
    f3= b.slider("Rating given by company",1,5)
    f4= b.number_input(label="Cost of product", format="%f")
    f5= b.slider("Prior Purchases",0,15)
    display1 = ("low", "medium","high")
    options1 = list(range(len(display1)))
    f6 = b.selectbox("Product Classification", options1, format_func=lambda x: display1[x])
    display2 = ("F","M")
    options2 = list(range(len(display2)))
    f7 = b.selectbox("Gender", options2, format_func=lambda x: display2[x])
    f8= b.number_input(label="Discount Offered", format="%f")
    f9= b.number_input(label="Weight in g", format="%f")

    inputs=[[f1,f2,f3,f4,f5,f6,f7,f8,f9]]

    if b.button('Predict'):
        b.success(Predict(data.predict(inputs)))
def Predict(num):
        if num == 0:
            return 'Will reach on time'
        else:
            return 'Possibilities of not reaching on time'

if __name__=='__main__':
    main()
