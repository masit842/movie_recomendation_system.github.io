
import streamlit as st

import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8ef160a1701ab9819744d293813b8165'.format(movie_id))
    data = response.json()
    print(data)

    return "https://image.tmdb.org/t/p/w185/"+ data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    recomennded_movie_poster=[]
    for i in movie_indices:
        movie_id = movies.iloc[i[0]].movie_id
        #poster fetch

        recommendations.append(movies.iloc[i[0]].title)
        recomennded_movie_poster.append(fetch_poster(movie_id))
    return recommendations,recomennded_movie_poster


# Load the similarity matrix and movies list
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pickle.load(open('movies.pkl', 'rb'))

# Ensure that 'movies' is a DataFrame and extract titles
movies_list = movies['title'].values

st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    'Which movie do you like the most?',
    movies_list
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3,col4,col5 = st.columns(5)

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

  
