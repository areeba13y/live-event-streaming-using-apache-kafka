import streamlit as st
import pandas as pd

st.title("🚨 DDoS Detection Dashboard")

data = []

try:
    with open("alerts.json", "r") as f:
        for line in f:
            data.append(eval(line))
except:
    st.write("No alerts yet")

if data:
    df = pd.DataFrame(data)
    st.write(df)

    st.bar_chart(df["ip"].value_counts())
else:
    st.write("Waiting for alerts...")