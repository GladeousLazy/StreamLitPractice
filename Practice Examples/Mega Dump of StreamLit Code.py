#This app is specifically created to learn and test streamlit codes

import streamlit as st
import numpy as np
import pandas as pd

#st.title("My First App")

#st.write("""Just some text to see how it looks!. Now for the tricky stuff""")

#st.write(pd.DataFrame({
#    'First Column':[1,2,3,4],
#    'Second Column': [10,20,30,40]
#}))


"""
# My first App
Just some text to see how it looks!. Now for the tricky stuff

"""
st.write("""# Table""")
df = pd.DataFrame(
    {
    'First Column':[1,2,3,4],
    'Second Column' : [10,20,30,40]
    }
)

df


chart_data = pd.DataFrame(
np.random.randn(20,3),
columns = ['a','b','c']
)
st.write("""# Line Chart""")
st.line_chart(chart_data)



map_data = pd.DataFrame(
np.random.randn(1000,2)/ [50,50] + [37.64, -122.4],
columns = ['lat','lon']
)
st.write("""# Map Chart""")
st.map(map_data)



st.write("""# Checkbox""")
if st.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns = ['a','b','c']
    )
    chart_data


st.write("""# Select box/Filter""")
option = st.selectbox(
    'Which number do you like best?',
    df['First Column']
)
'You selected ', option

st.write("""# Sidebar""")
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Wohooo!")

expander = st.beta_expander('FAQ')
expander.write("Here you can put in some really, really loong explaination...")


import time

'Starting a long computation...'

#Add a Place Holder

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    #Update the progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'...and now we are done!'
