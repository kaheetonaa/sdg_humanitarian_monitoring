import streamlit as st
import pandas as pd
import numpy as np
from pymongo import MongoClient

st.set_page_config(layout="wide")

@st.cache_resource
def init_connection():
    return MongoClient("mongodb+srv://kuquanghuy:quanghuy123456@cluster0.6mzug.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = init_connection()

db=client['SDG-Humanitarian-Mapping']
collection=db['SDG-Humanitarian-Mapping']
platform = st.selectbox('Select Humanitarian Mapping Platform',['All','HOT-TM','Ushahidi','Mapswipe'])

all_data=pd.DataFrame(list(collection.find({})))

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

df2=df2.fillna(' ')#replace nan with -

for i in range(len(df_selected_indicators['Indicator'])):
    indicator=df_selected_indicators['Indicator'][i]
    k= int(indicator.split('.')[0])-1
    j=df2[columns[k]].str.contains(indicator)
    level=0 #0= enhanced by GI, 1= enhanced by HM, 2= added by HM
    project=0 #0 non project exist, project existed
    if (platform=='All'):
        if (collection.find_one({'indicators':indicator})!=None):
            project=1
        if df_selected_indicators['HM-A'][i]==True:
            level=2
        if df_selected_indicators['HM-E'][i]==True:
            level=1
    else:
        if (collection.find_one({'indicators':indicator,'platform':platform})!=None):
            project=1
        if df_selected_indicators['HM-A'][i]==True:
            level=2
        if df_selected_indicators['HM-E'][i]==True:
            level=1

    for l in range(len(j)):
        match level:
            case 0:
                color='lightgray'
            case 1:
                color='#E0F8FF'
            case 2:
                color='#62CBEC'
        match project:
            case 0:
                stroke=' '
            case 1:
                stroke=' solid '

        if j[l]==True:
            df2.loc[l,columns[k]]="<span style='display: inline-block; padding: .2em .5em .3em; border:2px"+stroke+"#1C2E33; border-radius: 10px; background: "+color+"; color: #1C2E33; font-weight: 600; margin: .25em .1em'>"+df2.loc[l,columns[k]]+"</span>"
    #Rendering

st.title('SDG and Humanitarian Mapping Monitoring')
st.write('---')
st.markdown(df2.style.hide(axis = 0).hide(axis = 1).to_html(), unsafe_allow_html = True)

df_selected_indicators

all_data