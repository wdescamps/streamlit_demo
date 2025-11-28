import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go


st.markdown("""# This is a header
## This is a sub header
This is text""")

df = pd.DataFrame({
    'first column': list(range(1, 11)),
    'second column': np.arange(10, 101, 10)
})

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 3, 10, 3)

# and used to select the displayed lines
head_df = df.head(line_count)


def get_plotly_data():

    z_data = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/api_docs/mt_bruno_elevation.csv')
    z = z_data.values
    sh_0, sh_1 = z.shape
    x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
    return x, y, z


x, y, z = get_plotly_data()

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title='IRR', autosize=False, width=800, height=800, margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)

head_df