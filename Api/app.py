# flask_ngrok_example.py
from flask import Flask,request,jsonify


import pickle
app = Flask(__name__)
 # Start ngrok when app is run
import pandas as pd
new_df=pd.read_csv('./Users.csv')

import random
import numpy as np

similarity=pickle.load(open('similarity.pkl','rb'))
print(similarity[0])

def find_similarity(data):
    # users_df=data
    # print("users data: ",users_df)
    # # users_relevant = ['bio','college','dob','face_detection_probabilities','createdAt', 'gender', 
    # #               'interests' ,'status','updatedAt','who_to_date','is_subscribed','is_habit_drink',
    # #               'is_habit_smoke','is_verified','name']
    # # users_df = users[users_relevant]
    # # users_df  = users_df.drop(users_df[users_df.status==False].index)
    # # users_df['who_to_date'].fillna("A", inplace = True)
    # import re
    # def format_interests(s):
    #   return re.sub("\"|\[|\]|\'", "", s)
    # users=users_df
    # # users['interests'] = users.interests.apply(lambda x: format_interests(str(x)))
    # # users['college'] = users.college.apply(lambda x: format_interests(str(x)))
    
    # # users['dob'] = pd.to_datetime(users['dob']).dt.strftime('%Y-%m-%d')
    # # users['age'] = users['dob'].apply(lambda x: pd.to_datetime('today').year - pd.to_datetime(x).year)
    # tags=""
    # tags+=users['college']
    
    # if users['gender']=="M":
    #     tags+=" "+"Male"
    # if users['gender']=="F":
    #     tags+=" "+"Female"
    # if users['gender']=="NB":
    #     tags+=" "+"Non Binary"
    # # users['gender']=users['gender'].replace(to_replace="M",value="Male")
    # # users['gender']=users['gender'].replace(to_replace="F",value="Female")
    # # users['gender']=users['gender'].replace(to_replace="NB",value="Non Binary")
    # if users['who_to_date']=="M":
    #     tags+=" "+"Male"
    # if users['who_to_date']=="F":
    #     tags+=" "+"Female"
    # if users['who_to_date']=="NB":
    #     tags+=" "+"Non Binary"
    # if users['who_to_date']=="A":
    #     tags+=" "+"Anyone"
    
    # if users['is_habit_drink']=="O":
    #     tags+=" "+"Drink"
    # if users['is_habit_drink']=="S":
    #     tags+=" "+"Social"
    # if users['is_habit_smoke']=="O":
    #     tags+=" "+"Smoke"
    # if users['is_habit_smoke']=="S":
    #     tags+=" "+"Social"
    
    
    
    # # users.who_to_date=users.who_to_date.replace(to_replace="M",value="Male")
    # # users.who_to_date=users.who_to_date.replace(to_replace="F",value="Female")
    # # users.who_to_date=users.who_to_date.replace(to_replace="A",value="Anyone")
    # # users.who_to_date=users.who_to_date.replace(to_replace="NB",value="Non Binary")
    # # users.is_habit_drink=users.is_habit_drink.replace(to_replace="N",value="")
    # # users.is_habit_drink=users.is_habit_drink.replace(to_replace="O",value="Drink")
    # # users.is_habit_drink=users.is_habit_drink.replace(to_replace="S",value="Social")
    # # users.is_habit_smoke=users.is_habit_smoke.replace(to_replace="N",value="")
    # # users.is_habit_smoke=users.is_habit_smoke.replace(to_replace="O",value="Smoke")
    # # users.is_habit_smoke=users.is_habit_smoke.replace(to_replace="S",value="Social")
    
    # if users['is_verified']:
    #     tags+=" Verified"
        
    # # users.is_verified=users.is_verified.apply(ver)
    # # users.is_subscribed=users.is_subscribed.apply(lambda x:str(x))
    # # users.is_subscribed=users.is_subscribed.replace(to_replace="True",value="Subscribed")
    # # users.is_subscribed=users.is_subscribed.replace(to_replace="nan",value="")
    # if str(users['is_subscribed'])=="True":
    #     tags+=" True"
        
    # users['tags']=users['bio']+" "+users['clg']+" "+" "+users['gender']+" "+users['is_habit_drink']+" "+users['is_habit_smoke']+" "+users['is_subscribed']+" "+users['is_verified']+" "+users['name']+" "+users['who_to_date']
    # users.tags=users.tags.replace(to_replace="\n",value=" ")
    # temp={
    #     "_id":users['_id'],
    #     "name":users['name'],
    #     "tags":tags
    # }
    # df = pd.DataFrame(temp)
    
    # # display(df)
    
    # # df2 = {'Name': 'Amy', 'Maths': 89, 'Science': 93}
    # df = df.append(df2, ignore_index = True)
    
    # display(df)
    return similarity[random.randint(0,1404)][random.randint(0,1404)]
    


def new_score(data):
    score= 0
    new_df=data
    if new_df['verified_at']:
        score+= 20
    
    if new_df['is_subscribed']:
        score += 30

    if new_df['face_detection_probabilities']!=np.nan:
        score+=10
    n=random.randint(0,1404)
    
    one_user=find_similarity(data)
    cos=int(one_user)
    score+=min(cos,20)

    return score

def recommend_profiles(profile_score, num_recommendations):
    # Get the latest 100 profiles
    # users['createdAt'] = pd.to_datetime(users['createdAt'])
    
    cols=['first_like_unlike_at','first_type','is_unmatch','like_count','p1','p2','second_like_unlike_at','second_type','unmatch_on']
    # url2="https://raw.githubusercontent.com/kushalpoddar/idyll-dummy-dataset/main/swipes.csv"
    swipes=pd.read_csv('./swipes.csv',low_memory=False)
    swipes=swipes[cols]
    swipes.info()

    swipes['unmatch_on'].isna().sum()

    swipes.isna().sum()

    swipes.p1.value_counts()

    swipes.p2.value_counts()

    swipes.p1.isna().sum()

    swipes = swipes.sort_values(by=['p1', 'first_like_unlike_at'], ascending=[True,True])
    swipes.head()

    def count(col:str):
        likes = {}
        dislikes = {}
        for id in range(1405):
            data = swipes[swipes[col]==id]
            # print(data.shape)
            
            l = 0
            d = 0
            for i in range(data.shape[0]):
                if data.iloc[i, 1] == "LIKE":
                    l += 1
                else:
                    d += 1
            
            likes[id] = l
            dislikes[id] = d
        
        return likes, dislikes

    p1_likes, p1_dislikes = count('p1')
    p2_likes, p2_dislikes = count('p2')

    print(p1_likes[0])
    print(p1_dislikes[0])
    print(p2_likes[0])
    print(p2_dislikes[0])

    p1_like_dislike = {}
    p2_like_dislike = {}
    p1_like_p2_like = {}

    def div(n,d):
        if d==0:
            return n
        else:
            return n/d

    for i in range(1405):
        if p1_dislikes[i] == 0:
            p1_dislikes[i] += 1

        p1_like_dislike[i] = div(p1_likes[i], p1_dislikes[i])
        if p1_like_dislike[i] > 45:
            print(i, p1_like_dislike[i])
        p2_like_dislike[i] = div(p2_likes[i], p2_dislikes[i])
        p1_like_p2_like[i] = div(p1_likes[i], p2_likes[i])

    print(p1_like_dislike[0])
    print(p2_like_dislike[0])
    print(p1_like_p2_like[0])

    interaction = pd.DataFrame({
    'p1 likes': p1_likes,
    'p2 likes': p2_likes,
    'p1 dislikes': p1_dislikes,
    'p2 dislikes': p2_dislikes,

    'p1 likes / p1 dislikes':p1_like_dislike,
    'p1 likes / p2 dilikes': p2_like_dislike,
    'p1 likes / p2 likes': p1_like_p2_like
    })

    from sklearn import preprocessing

    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(interaction)
    interaction_scaled = pd.DataFrame(x_scaled, columns=interaction.columns)
    interaction_scaled.describe()

    swipes['p1'].value_counts()

    swipes['unmatch_on'] = pd.to_datetime(swipes['unmatch_on'])
    swipes['first_like_unlike_at'] = pd.to_datetime(swipes['first_like_unlike_at'])
    swipes['second_like_unlike_at'] = pd.to_datetime(swipes['second_like_unlike_at'])
    swipes.info()

    profiles=[]
    for i in range(1405):
        temp=swipes[swipes['p1']==i]
        profiles.append(temp)

    matches={}

    for i in range(0,1405):
        count=0
        # print(profiles1[i])
        df=profiles[i]
        for j in range(len(df)):

            if df['first_type'].iloc[j]=="LIKE" and df['second_type'].iloc[j]=="LIKE":
                count+=1
        matches[i]=count

    print(matches[0])

    len(['bio', 'college', 'dob',
        'face_detection_probabilities', 'gender', 'height',
        'interests', 'is_habit_drink', 'is_habit_smoke',
        'what_to_find', 'who_to_date'])

    complete_profile_cols = ['']

    users_relevant = ['createdAt', 'gender', 'interests' , 'is_verified', 'status', 'updatedAt', 'who_to_date', 'is_subscribed']
    users=new_df
    users_df = users[users_relevant]
    users_df

    users_df["interests"][0]

    users_df.isnull().sum()

    users_df['status'].sum()

    users_df.isnull().sum()

    users_df  = users_df [users_df ['gender'].notna()]

    users_df['who_to_date'].fillna("A", inplace = True)

    users_df.head()

    # users_df['interests'] = users_df['interests'].apply(lambda x: x.split(','))

    users_df.head()

    users_df[users_df.index==170]

    users_df['is_subscribed'].value_counts()

    comp100_profile = ['bio', 'college', 'dob', 'face_detection_probabilities', 'gender', 'height', 'interests', 'is_habit_drink', 'is_habit_smoke', 'what_to_find', 'who_to_date']

    users.head()

    def existing_score():
        scores = {}
        for i in range(1405):
            score = 0
            if users['verified_at'].iloc[i]:
                score += 10
            
            if users['is_subscribed'].iloc[i]:
                score += 20
            
            # score += 5
            score += users[comp100_profile].iloc[i, :].notna().sum()

            score += min(matches[i] * 2, 10)

            score += min(interaction_scaled.iloc[i, 0] * 100, 10) #P1
            score += min(interaction_scaled.iloc[i, 1] * 100, 10) #P2

            score += min(interaction_scaled.iloc[i, 2] * 100, 10) #P1 - DIS
            score -= min(interaction_scaled.iloc[i, 3] * 100, 10) #P2 - DIS

            score += min((interaction_scaled.iloc[i, 1] + interaction_scaled.iloc[i, 0]) * 100, 5)

            # score += len(users['interests'].iloc[i].split(','))
            
            scores[i] = score
        return scores

    users['score'] = existing_score().values()
    
    
    latest_profiles = new_df['createdAt'].sort_values(ascending=False)[:100]

    # print(latest_profiles)
    # Shuffle the profiles
    random.shuffle(list(latest_profiles))
    
    # Calculate the score range for the user
    score_range = (profile_score - 20, profile_score + 20)

    # Filter the profiles based on score range
    # print(latest_profiles.index[0])
    # print(users.iloc[latest_profiles.iloc[0]].index)
    # print(users['score'].iloc[1] >= score_range[0] and users['score'].iloc[1] <= score_range[1])
    new_df=pd.read_csv('./final_users.csv')
    filtered_profiles = list(filter(lambda x: new_df['score'].iloc[x] >= score_range[0] and new_df['score'].iloc[x] <= score_range[1], latest_profiles.index))
    
    # Sort the profiles by match count in ascending order
    # print(filtered_profiles)
    sorted_profiles = sorted(filtered_profiles, key=lambda x: new_df['matches'].iloc[x])
    
    # Add a bias towards free accounts and low match counts
    biased_profiles = []
    counter1, counter2 = 0, 0
    for profile in sorted_profiles:
        if isinstance(new_df['is_subscribed'].iloc[profile], float): # denotes null values (not subscribed)
            # Add free accounts multiple times to increase visibility
            # biased_profiles += [profile] * 2
            biased_profiles.append(profile)
            counter1+=1

        elif new_df['matches'].iloc[profile] <= 1:
            # Add profiles with low match counts multiple times to increase visibility
            # biased_profiles += [profile] * 2
            biased_profiles.append(profile)
            counter2+=1
        
        if counter1==2 or counter2==2:
            biased_profiles.append(profile)
            counter1, counter2 = 0, 0
    
    # Take the top num_recommendations profiles
    recommended_profiles = biased_profiles[:num_recommendations]
    
    return recommended_profiles


@app.route("/recommend",methods=['GET','POST'])
def hello():
    data=request.json
    for key in data.keys():
        key=key.replace('\"','')
    print(data)
    _id=data['_id']
    print(_id)
    if _id>1404:
        profile_score = new_score(data)
        ids = recommend_profiles(profile_score, 10)
        # 
        # i=_id
        # score= 0
        # if new_df['verified_at'].iloc[i]:
        #     score+= 20
        
        # if new_df['is_subscribed'].iloc[i]:
        #     score += 30

        # if new_df['face_detection_probabilities'].iloc[i]!=np.nan:
        #     score+=10
        # n=random.randint(0,1404)
        
        # cos=int(similarity[i][n]*30)
        # score+=min(cos,20)

        # return score
        # 
        
    else:
        # movie_index=new_df[new_df['_id']==_id].index[0]
        distances=similarity[_id]
        print("Similarity: ",distances)
        movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
        print(movies_list)
        ans=[]
        for i in movies_list:
            ans.append(i[0])
        print("ans",ans)
        final={}
        for c,i in enumerate(ans):
            final[c]=new_df[new_df['_id']==i].to_dict()
        return final  

    
    # return jsonify(data)
    

if __name__ == '__main__':
    # app.run(debug=True)
     app.run(host="0.0.0.0")