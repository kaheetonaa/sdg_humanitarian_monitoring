import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

st.write("This is :blue[test]")

data_df = pd.DataFrame(
    {
        "name":['a','b','c','d'],
        "sales": [
            ["This is :blue[test]", '4', '26', '80', 'a', '40'],
            ["This is :blue[test]", '4', '26', '80', 'a', '40'],
            ["This is :blue[test]", '4', '26', '80', 'a', '40'],
            ["This is :blue[test]", '4', '26', '80', 'a', '40'],
        ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "name": st.column_config.TextColumn(
        "Name", help="The name of the user", max_chars=100
    ),
        "sales": st.column_config.ListColumn(
            "Sales (last 6 months)",
            help="The sales volume in the last 6 months",
            width="large",
        ),
    },
    hide_index=True,
)

np.random.seed(0)
df2 = pd.DataFrame(np.random.randn(10,4), columns=['A','B','C','D'])
df2.style

def style_negative(v, props=''):
    return props if v < 0 else None
s2 = df2.style.map(style_negative, props='color:red;')\
              .map(lambda v: 'opacity: 20%;' if (v < 0.3) and (v > -0.3) else None)

def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')
s2.apply(highlight_max, props='color:white;background-color:darkblue', axis=0)  

s2