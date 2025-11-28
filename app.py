import streamlit as st
import pandas as pd

df = pd.read_csv("data/train.csv")

inputs = {}

for col in df.columns:
    if col == "price":
        continue
    col_alias = col.capitalize().replace("_"," ")
    if df[col].dtype in ["float64","int64"]:
        inputs[col]=st.number_input(col_alias)
    else:
        options = df[col].unique().tolist()
        inputs[col]=st.selectbox(col_alias,options)