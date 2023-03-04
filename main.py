import json
import pickle
import numpy as np
import pandas as pd
import streamlit as st

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

users = pd.read_csv('./Users.csv')

# pkl = open("", "rb")
# model = pkl.load(pkl)

def welcome():
    return "Welcome!"

# def predict():
#     prediction = model.predict([])
#     return prediction

def main():
    vert_space = "<body style='bgcolor: \"pink\";'></body>"
    st.markdown(vert_space, unsafe_allow_html=True)
    # st.sidebar.title("Navigation Bar")
    user_menu=st.sidebar.radio('Select an Option', ('Home','Suggestions','Overall Analysis'))

    if(user_menu=='Home'):
        st.title("PROFILE SCORING!")
        st.markdown('Provide the follwing data')
        data = st.text_area("Data (json):", {})
        st.json(json.loads(data))
    
    elif(user_menu=='Overall Analysis'):
        st.header('Overall Analysis')
        col1, col2 = st.columns(2)
        col1.subheader("Verifed Users")
        col1.plotly_chart(px.pie(users, values='_id', names='is_verified'), use_container_width=True)
        
        col2.subheader("Subcribed Users")
        col2.plotly_chart(px.pie(users, values='_id', names='is_subscribed'), use_container_width=True)
        
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
        st.header('Suggestions')
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