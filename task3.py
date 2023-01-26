import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("titles.csv")
sf = pd.read_csv("credits.csv")


def show_procents_good_movies(df):
    new_films = df[df['release_year'] >= 2000]

    years = list(new_films['release_year'].unique())
    years.sort()

    good_movies_procents = []

    for year in years:
        movies_count = len(df[df['release_year'] == year])
        movies_good_rate_count = len(df[(df['release_year'] == year) & (df['imdb_score'] >= 8)])
        procent_of_good_movies = movies_good_rate_count / (movies_count / 100)
        good_movies_procents.append(procent_of_good_movies)

    plt.plot(years, good_movies_procents)
    plt.show()

    best_procent = max(good_movies_procents)

    index_best_procents = good_movies_procents.index(best_procent)

    print(f"Best year is {years[index_best_procents]}")


def run_third_task(df):
    show_procents_good_movies(df)


run_third_task(df)
