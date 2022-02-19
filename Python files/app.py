import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_new[movies_new['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    print("Recommended movies are:")
    for i in movie_list:
        print(movies_new.iloc[i[0]].title)

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie', ( movies['title'].values))

if st.button('Recommend'):
    st.write('Hello')