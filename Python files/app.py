import streamlit as st
import pickle
import pandas as pd

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

st.title('Movie Recommender System')

selected_movie = st.selectbox('Select a movie', ( movies['title'].values))
