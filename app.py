import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly"

st.markdown("""
Definition of key metrics:
- Value: Median wage of postings with the associated skill
- Growth: Weighted year on year growth of skill frequency (divided by total number of posts collected) 
- Difficulty: a measure of skill sophistication where higher values indicate use in more complex occupation.      
            """)

tab1, tab2, tab3 = st.tabs(['**VALUE vs GROWTH visual**','**DIFFICULTY vs GROWTH visual**', '**DIFFICULTY vs VALUE visual**'])

with tab1:
    data_df = pd.read_csv('dynamic_ssg_clusters.csv')
# Renaming the numerical labels to actual labels and converting to strings
    data_df['GROWTH_KME'] = data_df['GROWTH_KME'].map({1:'High Growth', 0: 'Low Growth'})
    data_df['VALUE_KME'] = data_df['VALUE_KME'].map({1: 'High Value', 0: 'Low Value'})
    data_df['GROWTH_KME'] = data_df['GROWTH_KME'].astype(str)
    data_df['VALUE_KME'] = data_df['VALUE_KME'].astype(str)

# Concatenate 'VALUE_KME' and 'GROWTH_KME' for color
    data_df['Value_Growth_Clusters'] = data_df['VALUE_KME'] + '_' + data_df['GROWTH_KME'].astype(str)

    fig = px.scatter(data_df, x='VALUE', y='GROWTH', color='Value_Growth_Clusters', hover_name='LIGHTCAST_SKILL',title='VALUE vs GROWTH')
    fig.update_layout(width=900, height=600) 
    st.plotly_chart(fig)
    
with tab2:
    data_df = pd.read_csv('dynamic_ssg_clusters.csv')
# Renaming the numerical labels to actual labels and converting to strings
    data_df['GROWTH_KME'] = data_df['GROWTH_KME'].map({1:'High Growth', 0: 'Low Growth'})
    data_df['DIFFICULTY_KME'] = data_df['DIFFICULTY_KME'].map({1: 'High Difficulty', 0: 'Low Difficulty'})
    data_df['GROWTH_KME'] = data_df['GROWTH_KME'].astype(str)
    data_df['DIFFICULTY_KME'] = data_df['DIFFICULTY_KME'].astype(str)

# Concatenate 'DIFFICULTY_KME' and 'GROWTH_KME' for color
    data_df['Difficulty_Growth_Clusters'] = data_df['DIFFICULTY_KME'] + '_' + data_df['GROWTH_KME'].astype(str)

    fig = px.scatter(data_df, x='DIFFICULTY', y='GROWTH', color='Difficulty_Growth_Clusters', hover_name='LIGHTCAST_SKILL',title='DIFFICULTY vs GROWTH')
    fig.update_layout(width=900, height=600) 
    st.plotly_chart(fig)
    
with tab3:
    data_df = pd.read_csv('dynamic_ssg_clusters.csv')
# Renaming the numerical labels to actual labels and converting to strings
    data_df['VALUE_KME'] = data_df['VALUE_KME'].map({1:'High Value', 0: 'Low Value'})
    data_df['DIFFICULTY_KME'] = data_df['DIFFICULTY_KME'].map({1: 'High Difficulty', 0: 'Low Difficulty'})
    data_df['VALUE_KME'] = data_df['VALUE_KME'].astype(str)
    data_df['DIFFICULTY_KME'] = data_df['DIFFICULTY_KME'].astype(str)

# Concatenate 'VALUE_KME' and 'DIFFICULTY_KME' for color
    data_df['Value_Difficulty_Clusters'] = data_df['VALUE_KME'] + '_' + data_df['DIFFICULTY_KME'].astype(str)

    fig = px.scatter(data_df, x='DIFFICULTY', y='VALUE', color='Value_Difficulty_Clusters', hover_name='LIGHTCAST_SKILL',title='DIFFICULTY vs VALUE')
    fig.update_layout(width=900, height=600) 
    st.plotly_chart(fig)
    
    




