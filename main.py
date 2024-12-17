import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")



columns=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q']
np.random.seed(0)
df2 = pd.DataFrame(columns=columns) #np.zeros(shape=(15,17)).astype('U'),
df1=pd.read_csv('assets/241217-SDG-Indicators.csv')
df1['Indicators'][3].split('.')
df_selected_indicators=pd.read_csv('assets/Selected_Indicators.csv')



for i in range(17):
    if i<9:
        df2.loc[0,columns[i]]="<img src='https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-0"+str(i+1)+".jpg'></img>"
    else:
        df2.loc[0,columns[i]]="<img src='https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-"+str(i+1)+".jpg'></img>"
#heading
ind=[1 for i in range(17)]
for i in df1['Indicators']:
    k= int(i.split('.')[0])-1
    df2.loc[ind[k],columns[k]]=str(i)
    ind[k]=ind[k]+1
#putting in indicators

for i in df_selected_indicators['Indicator']:
    k= int(i.split('.')[0])-1
    j=df2[columns[k]].str.contains(i)
    for l in range(len(j)):
        if j[l]==True:
            df2.loc[l,columns[k]]="<span style='display: inline-block; border-radius: 3px; padding: .2em .5em .3em; border-radius: 2px; background: blue; color: white; font-weight: 600; margin: .25em .1em'>"+df2.loc[l,columns[k]]+"</span>"

#df2.loc[2,'B']="<span style='display: inline-block; border-radius: 3px; padding: .2em .5em .3em; border-radius: 2px; background: darkgreen; color: white; font-weight: 600; margin: .25em .1em'>1.1.1</span>"
st.title('SDG and Humanitarian Mapping Monitoring')
st.write('---')
st.markdown(df2.style.hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

df_selected_indicators