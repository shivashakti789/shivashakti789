import streamlit as st 
import pandas as pd 
import pickle 

df = pickle.load(open('df.pkl' , 'rb'))
similarity  = pickle.load(open('similarity.pkl' , 'rb'))

#recommendation 

def recommandation(title):
    idx= df[df['Title'] == title].index[0]
    idx = df.index.get_loc(idx)
    distance = sorted(list(enumerate(similarity[idx])), key = lambda x:x[1], reverse = True)[1:11]
    
    jobs = []
    for i in distance:
        jobs.append(df.iloc[i[0]].Title)
    return jobs 
    


#web application 

st.title('JOB Recommendation App')
title = st.selectbox('Search Job', df['Title'])


jobs = recommandation(title)

if jobs:
    st.write(jobs)
