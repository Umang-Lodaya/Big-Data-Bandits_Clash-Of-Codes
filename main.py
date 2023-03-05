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
    st.sidebar.image("https://www.getidyll.in/assets/logo-1.svg")
    # st.sidebar.title("IDLLY!")
    vert_space = "<body style='bgcolor: \"pink\";'></body>"
    st.markdown(vert_space, unsafe_allow_html=True)
    # st.sidebar.title("Navigation Bar")
    user_menu=st.sidebar.radio('Select an Option', ('Home','Recommendations','Exploratory Data Analysis', 'Suggestions & Future Scope'))

    if(user_menu=='Home'):
        st.header("FIND YOUR PERFECT MATCH!")
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
        col1.plotly_chart(px.pie(users, values='_id', names='is_habit_drink', color_discrete_sequence=["pink", "purple"]), use_container_width=True)
        
        col2.subheader("Smoking Habits")
        col2.plotly_chart(px.pie(users, values='_id', names='is_habit_smoke', color_discrete_sequence=["pink", "purple"]), use_container_width=True)
        
        
        col1, col2 = st.columns(2)
        col1.subheader("What to Find")
        col1.plotly_chart(px.pie(users, values='_id', names='what_to_find', color_discrete_sequence=["pink", "purple"]), use_container_width=True)
        
        # vert_space = '<div style="padding: 30px 150px;"></div>'
        # st.markdown(vert_space, unsafe_allow_html=True)

        col2.subheader("Age")
        col2.plotly_chart(px.line(users, x="_id", y="age", color_discrete_sequence=["pink", "purple"]), use_container_width=True)

    elif (user_menu == 'Suggestions & Future Scope'):
        st.write('## Suggestions:')
        st.write("""Using a drop down menu to enter college information (Improve the data collection and analysis).
                    \n
Should not be utilised as a loading animation (It can confuse the user and cross and like animation should be used for like and dislike)
                    \n
More female consumers should be drawn to the platform, since this will immediately boost the male audience.
                    \n
Displaying pop-ups with relationship advice (free user gets 3-5 pop up per day and we can ask them to take pro membership to avail more tips and more features)
                    \n
According to us, no insta id should be used because it might reduce the user's time and engagement.""")
        
        st.write("During our testing, we discovered a problem in which a female account received more likes than a free account and was also able to see who liked, despite the fact that they are intended to be pro features.")
    
        st.write('## Future Scope')
        st.write("""We can apply multiple policies/algo for scoring and recommendations system and we can randomly use any policy and then record the feedback for it and using reinforcement learning do exploration and exploitation to select best policy""")
    else:
        st.header('Recommendations')


        col1, col2, col3, col4, col5 = st.columns(5)
        
        for i in [0, 5]:
            # col1.subheader("User " + str(i+1))
            hasClicked = card(
        title="User " + str(i+1),
        text="Some description",
        # image="http://placekitten.com/200/300",
        url="https://github.com/gamcoh/st-card"
        )
            # col1.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
            # col2.subheader("User " + str(i+2))
            hasClicked = card(title="User " + str(i+2), text="Some description",)
        
            # col2.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
            # col3.subheader("User " + str(i+3))
            hasClicked = card(
        title="User " + str(i+3),
        text="Some description",
        # image="http://placekitten.com/200/300",
        url="https://github.com/gamcoh/st-card"
        )
            # col3.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
            # col4.subheader("User " + str(i+4))
            hasClicked = card(
        title="User " + str(i+4),
        text="Some description",
        # image="http://placekitten.com/200/300",
        url="https://github.com/gamcoh/st-card"
        )
            # col4.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
            # col5.subheader("User " + str(i+5))
            hasClicked = card(
        title="User " + str(i+5),
        text="Some description",
        # image="http://placekitten.com/200/300",
        url="https://github.com/gamcoh/st-card"
        )
            # col5.plotly_chart(px.pie(users, values='_id', names='is_subscribed', color_discrete_sequence=["pink", "purple"][::-1]), use_container_width=True)
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