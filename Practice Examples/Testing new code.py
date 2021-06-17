import streamlit as st
import pandas as pd
import numpy as np

dataframe = pd.DataFrame(
np.random.randn(10,20),
columns = ('col %d' % i for i in range(20)))

#st.dataframe(dataframe.style.highlight_max(axis = 0))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
#st.table(dataframe)

x = st.slider('x')
st.write(x, 'squared is:', x * x)



add_selectbox = st.sidebar.selectbox(
'How would you like to be contacted?',
('Email','Home Phone','Mobile Phone')
)

add_slider = st.sidebar.slider(
'Select a range of values',
0.0, 100.0, (25.0,75.0)
)

left_column, right_column = st.beta_columns(2)

if left_column.button('Presssss ME!!!!'):
    st.write('Now why did you do that?!')

with right_column:
    chosen = st.radio(
    'Sorting hat',
    ("Griffindor","Ravenclaw","Hufflepuff","Slytherin"))
    st.write(f'You have chosen {chosen} house!')
