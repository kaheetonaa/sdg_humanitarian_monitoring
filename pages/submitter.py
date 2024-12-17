import streamlit as st
import pandas as pd
import requests
from streamlit_tags import *
from pymongo import MongoClient

st.set_page_config(layout="wide")

@st.cache_resource
def init_connection():
    return MongoClient("mongodb+srv://kuquanghuy:quanghuy123456@cluster0.6mzug.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = init_connection()

db=client['SDG-Humanitarian-Mapping']
collection=db['SDG-Humanitarian-Mapping']

print()

ind_dataset=pd.read_csv('assets/Selected_Indicators.csv')

platform = st.selectbox('Select Humanitarian Mapping Platform',['HOT-TM','Ushalhidi'])

code=st.text_input(label='input project code here')

if code:
    match platform:
        case 'HOT-TM':
            data=requests.get('https://tasking-manager-tm4-production-api.hotosm.org/api/v2/projects/'+code+'/').json()
            st.write('Link: https://tasks.hotosm.org/projects/'+code)
            st.write('Name:'+data['projectInfo']['name'])
            st.write('Name:'+data['projectInfo']['shortDescription'])
            st.write('Status:'+data['status'])
            st.write('Priority:'+data['projectPriority'])
            st.write('Difficulty:'+data['difficulty'])
        case 'Ushalhidi':
            st.write("Link: https://"+code+".ushahidi.io/map")
    indicators = st_tags(label='Enter indicators contributed by the project here')
    if indicators:
        if len(indicators)>0:
            st.write(ind_dataset[ind_dataset['Indicator'].isin(indicators)]['Indicators'])

    
if st.button('Submit'):
    if (collection.find_one({'platform':platform,'code':code})==None):
        post={'platform':platform,'code':code,'indicators':indicators}
        collection.insert_one(post)
        st.write('Submitted')
    else:
        st.write('Existed. Not submit. Please check the database')
   #check submitted
   #input

st.dataframe(ind_dataset)