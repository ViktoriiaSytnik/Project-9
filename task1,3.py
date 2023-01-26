import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("titles.csv")
sf = pd.read_csv("credits.csv")


def show_movies_hist(df):
    movies = df[df["type"] == 'MOVIE']
    movie_scores = movies['imdb_score']
    plt.hist(movie_scores, bins=40)
    plt.show()

    print(f"The best movie:\n{movies[movies['imdb_score'] == movies['imdb_score'].max()]['title']}")


def show_shows_hist(df):
    shows = df[df["type"] == 'SHOW']
    shows_scores = shows['imdb_score']

    plt.hist(shows_scores, bins=40)
    plt.show()

    print(f"The best show:\n{shows[shows['imdb_score'] == shows['imdb_score'].max()]['title']}")


def run_first_task(df):
    show_movies_hist(df)
    show_shows_hist(df)


run_first_task(df)
