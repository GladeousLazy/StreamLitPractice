import streamlit as st
import pandas as pd
import numpy as np

st.title("Uber Pickups in NYC")

DATE_COLUMN = "date/time"
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows = nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis = 'columns', inplace = True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

#Create a text element and let the read know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into dataframe
data = load_data(10000)
#Norify the reader that teh data was successfully loaded.
data_load_state.text('Done! (using st.cache)')
