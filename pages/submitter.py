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

platform = st.selectbox('Select Humanitarian Mapping Platform',['HOT-TM','Ushahidi','Mapswipe'])

code=st.text_input(label='input project code here')

if code:
    match platform:
        case 'HOT-TM':
            data=requests.get('https://tasking-manager-production-api.hotosm.org/api/v2/projects/'+code+'/',headers={"accept":"application/json"}).json() #"Authorization":"TOK<TVRBek5ERTVPRGsuYUFkTlZnLkFZU3NCNnpyV3ZFeG5QdnIzOWo1WTJnYlRqdw==>
            #st.write(data)
            st.write('Link: https://tasks.hotosm.org/projects/'+code)
            st.write('Name:'+data['projectInfo']['name'])
            st.write('Short description:'+data['projectInfo']['shortDescription'])
            st.code('Description:'+data['projectInfo']['description'],wrap_lines =True,height=300)
            st.write('Status:'+data['status'])
            st.write('Priority:'+data['projectPriority'])
            st.write('Difficulty:'+data['difficulty'])
        case 'Ushahidi':
            st.write("Link: https://"+code+".ushahidi.io/map")
            usha_data=pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vTJbGpaOjy6iJwyL92c-s_Q2_8t8qwTe6THhb7LND-iv1AijzK5_yQrA-KFHS8xhpF55_YmEpqog23c/pub?gid=1903567796&single=true&output=csv')
            st.write(usha_data[usha_data['objectID']==code]['excerpt'])
        case 'Mapswipe':
            st.write("Mapswipe project")
    indicators = st_tags(label='Enter indicators contributed by the project here')
    if indicators:
        if len(indicators)>0:
            st.write(ind_dataset[ind_dataset['Indicator'].isin(indicators)]['Indicators'])

    
    if st.button('Submit'):
        if (collection.find_one({'platform':platform,'code':code})==None):
            post={'platform':platform,'code':code,'indicators':indicators}
            collection.insert_one(post)
            st.write('Submitted')
            st.balloons()
        else:
            st.write('Existed. Not submit. Please check the database')
            st.snow()
    #check submitted
    #input

    st.dataframe(ind_dataset)
