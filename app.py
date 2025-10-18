import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5YTIwYTA2OTRmZDRmN2M3ZWNjODVlZTViOGJhNDM4YiIsIm5iZiI6MTc2MDc5NTgxMC44NjcsInN1YiI6IjY4ZjM5Y2EyYTIwNDEyMWM1ZWJkODdiOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oMnSAHA8PonSUScUrImM9oetWH9w7EPveEIytJa4kB8"
    }
    response = requests.get(url, headers=headers)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+(data['poster_path'])

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommended_movies,recommended_movies_poster

st.write("App started...")
movies_dict=pickle.load(open('movies_dict.pkl', 'rb'))
st.write("Loaded movies dictionary...")
similarity=pickle.load(open('similarity.pkl','rb'))
st.write("Loaded similarity matrix...")
movies=pd.DataFrame(movies_dict)
st.write("Created DataFrame...")
title=movies['title'].values
st.title("Movie Recommender System")
selected_movie_name=option=st.selectbox("Pick one", title)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])