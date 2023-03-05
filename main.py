import json
import pickle
import numpy as np
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
# st_card('Completed Orders', value=76.4, show_progress=True)

import requests
from urllib import response

users = pd.read_csv('./Users.csv')

# pkl = open("", "rb")
# model = pkl.load(pkl)

def welcome():
    return "Welcome!"

# def predict():
#     prediction = model.predict([])
#     return prediction
from streamlit_card import card

URI = "https://c3b4-2409-40c0-28-699f-41d3-899a-fa53-6435.in.ngrok.io/"

def main():
    vert_space = "<body style='bgcolor: \"pink\";'></body>"
    st.markdown(vert_space, unsafe_allow_html=True)
    # st.sidebar.title("Navigation Bar")
    user_menu=st.sidebar.radio('Select an Option', ('Home','Recommendations','Exploratory Data Analysis'))

    if(user_menu=='Home'):
        st.title("PROFILE SCORING!")
        st.markdown('Provide the follwing data')
        data = st.text_area("Data (json):", {})
        st.json(json.loads(data))

        if st.button('Get Prediction'):
            user_menu = "Recommendations"
            response = requests.post(URI, data={})
            response = json.loads(response.text)
            st.markdown(response)

    elif(user_menu=='Exploratory Data Analysis'):
        st.header('Overall Analysis')
        col1, col2 = st.columns(2)
        col1.subheader("Verified Users")
        col1.plotly_chart(px.pie(users, values='_id', names='is_verified', color_discrete_sequence=["pink", "purple"]), use_container_width=True)
        
        col2.subheader("Subscribed Users")
        col2.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        
        col1, col2 = st.columns(2)
        col1.subheader("Drinking Habits")
        col1.plotly_chart(px.pie(users, values='_id', names='is_habit_drink'), use_container_width=True)
        
        col2.subheader("Smoking Habits")
        col2.plotly_chart(px.pie(users, values='_id', names='is_habit_smoke'), use_container_width=True)
        
        
        col1, col2 = st.columns(2)
        col1.subheader("What to Find")
        col1.plotly_chart(px.pie(users, values='_id', names='what_to_find'), use_container_width=True)
        
        # vert_space = '<div style="padding: 30px 150px;"></div>'
        # st.markdown(vert_space, unsafe_allow_html=True)

        col2.subheader("Age")
        col2.plotly_chart(px.line(users, x="_id", y="age"), use_container_width=True)

    else:
        st.header('Recommendations')
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.subheader("Verified Users")
        col1.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        
        col2.subheader("Subscribed Users")
        col2.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col3.subheader("Subscribed Users")
        col3.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col4.subheader("Subscribed Users")
        col4.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col5.subheader("Subscribed Users")
        col5.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.subheader("Verified Users")
        col1.plotly_chart(px.pie(users, values='_id', names='is_verified', color_discrete_sequence=["pink", "purple"]), use_container_width=True)
        
        col2.subheader("Subscribed Users")
        col2.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col3.subheader("Subscribed Users")
        col3.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col4.subheader("Subscribed Users")
        col4.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        col5.subheader("Subscribed Users")
        col5.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
        
        # years,country=helper.country_year_list(users)
        
        # selected_year=st.sidebar.selectbox("Select Year",years)
        # selected_country=st.sidebar.selectbox("Select Country",country)
        # medal_tally=helper.fetch_medal_tally(users,selected_year,selected_country)
        # if selected_year == 'Overall' and selected_country == 'Overall':
        #     st.title("Overall Tally")
        # if selected_year != 'Overall' and selected_country == 'Overall':
        #     st.title("Medal Tally in " + str(selected_year) + " Olympics")
        # if selected_year == 'Overall' and selected_country != 'Overall':
        #     st.title(selected_country + " overall performance")
        # if selected_year != 'Overall' and selected_country != 'Overall':
        #     st.title(selected_country + " performance in " + str(selected_year) + " Olympics")
        # if medal_tally.empty:
        #     st.title("No data Available")
        # else:
        #     st.table(medal_tally)


if __name__ == "__main__":
    main()