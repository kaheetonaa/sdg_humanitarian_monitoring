import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

columns=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
np.random.seed(0)
df2 = pd.DataFrame(np.zeros(shape=(15,17)).astype('U'), columns=columns)

for i in range(17):
    df2.loc[1,columns[i]]="<span style='display: inline-block; border-radius: 3px; padding: .2em .5em .3em; border-radius: 2px; background: darkgray; color: white; font-weight: 600; margin: .25em .1em'>1.1.1</span>"
    if i<9:
        df2.loc[0,columns[i]]="<img src='https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-0"+str(i+1)+".jpg'></img>"
    else:
        df2.loc[0,columns[i]]="<img src='https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-"+str(i+1)+".jpg'></img>"

df2.loc[2,'B']="<span style='display: inline-block; border-radius: 3px; padding: .2em .5em .3em; border-radius: 2px; background: darkgreen; color: white; font-weight: 600; margin: .25em .1em'>1.1.1</span>"
st.title('SDG and Humanitarian Mapping Monitoring')
st.write('---')
st.markdown(df2.style.hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)