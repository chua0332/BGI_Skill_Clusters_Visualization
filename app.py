import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.io as pio

pio.templates.default = "plotly"

st.markdown("""
Definition of key metrics:
- Value: Median wage of postings with the associated skill across 2020 - 2023
- Growth: Weighted year on year growth of skill frequency (divided by total number of posts collected for a *particular year*) 
- Difficulty: The composite of Education, Experience & Complexity
- Demand: Basically a proxy for skill frequency, whereby it counts the number of job postings the skill is appearing in across the years (2020-2023), and then taking the average
- Resilience: The composite of Ubiquity & Stability
            """)

tab1, tab2, tab3 = st.tabs(['**VALUE vs GROWTH visual**','**DIFFICULTY vs VALUE visual**', '**RESILIENCE vs GROWTH visual**'])

with tab1:
    st.subheader('Please feel free to zoom in and out of the graph')
    data_df = pd.read_csv('dimension_clusters_forTableau.csv')

# Concatenate 'Demand Cluster' and 'Growth Cluster' for color
    data_df['Value_Growth_Clusters'] = data_df['Value Cluster'] + '_' + data_df['Growth Cluster'].astype(str)
    
#Converting value to numberic and removing $ signs and ','
    data_df['Value'] = data_df['Value'].str.replace('$', '', regex=False)  # Setting regex=False since '$' is literal here
    data_df['Value'] = data_df['Value'].str.replace(',', '', regex=False)

# Convert to numeric
    data_df['Value'] = pd.to_numeric(data_df['Value'], errors='coerce')
    
#Creating the dropdown to select the clusters
    cluster_options = data_df['Value_Growth_Clusters'].unique().tolist()
    selected_cluster = st.multiselect('Select Value_Growth Clusters', cluster_options, default=cluster_options)
    
 # Filter data based on selected cluster
    filtered_data = data_df[data_df['Value_Growth_Clusters'].isin(selected_cluster)]

    fig = px.scatter(filtered_data, x='Value', y='Growth', color='Value_Growth_Clusters', hover_name='Lightcast Skill',hover_data = {'SSG_Skill': True},title='GROWTH vs DEMAND')
    fig.update_layout(width=900, height=800) 
    st.plotly_chart(fig)
    
with tab2:
    st.subheader('Please feel free to zoom in and out of the graph')
    data_df = pd.read_csv('dimension_clusters_forTableau.csv')

# Concatenate 'Value Cluster' and 'Difficulty Cluster' for color
    data_df['Value_Difficulty_Clusters'] = data_df['Value Cluster'] + '_' + data_df['Difficulty Cluster'].astype(str)
    
#Converting value to numberic and removing $ signs and ','
    data_df['Value'] = data_df['Value'].str.replace('$', '', regex=False)  # Setting regex=False since '$' is literal here
    data_df['Value'] = data_df['Value'].str.replace(',', '', regex=False)

# Convert to numeric
    data_df['Value'] = pd.to_numeric(data_df['Value'], errors='coerce')
    
#Creating the dropdown to select the clusters
    cluster_options = data_df['Value_Difficulty_Clusters'].unique().tolist()
    selected_cluster = st.multiselect('Select Value_Difficulty_Clusters', cluster_options, default=cluster_options)
    
 # Filter data based on selected cluster
    filtered_data = data_df[data_df['Value_Difficulty_Clusters'].isin(selected_cluster)]

    fig = px.scatter(data_df, x='Value', y='Difficulty', color='Value_Difficulty_Clusters', hover_name='Lightcast Skill',hover_data = {'SSG_Skill': True},title='VALUE vs DIFFICULTY')
    fig.update_layout(width=900, height=800) 
    st.plotly_chart(fig)
    
with tab3:
    st.subheader('Please feel free to zoom in and out of the graph')
    data_df = pd.read_csv('dimension_clusters_forTableau.csv')

# Concatenate 'Resilience Cluster' and 'Growth Cluster' for color
    data_df['Resilience_Growth_Clusters'] = data_df['Resilience Cluster'] + '_' + data_df['Growth Cluster'].astype(str)
    
#Creating the dropdown to select the clusters
    cluster_options = data_df['Resilience_Growth_Clusters'].unique().tolist()
    selected_cluster = st.multiselect('Select Resilience_Growth_Clusters', cluster_options, cluster_options)
    
 # Filter data based on selected cluster
    filtered_data = data_df[data_df['Resilience_Growth_Clusters'].isin(selected_cluster)]

    fig = px.scatter(data_df, x='Resilience', y='Growth', color='Resilience_Growth_Clusters', hover_name='Lightcast Skill', hover_data = {'SSG_Skill': True}, title='Resilience vs Growth')
    fig.update_layout(width=900, height=800) 
    st.plotly_chart(fig)
    

    
    
    




