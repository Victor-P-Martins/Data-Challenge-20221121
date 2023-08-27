from fastapi import FastAPI
from routers import get_top_10_actores, get_top_5_paises, get_list_genre_movies
from src import DataBase
import pandas as pd
import json

df_amazon_prime = pd.read_csv(r"amazon_prime_titles.csv", sep=",", encoding="utf-8")
df_netflix = pd.read_csv(r"netflix_titles.csv", sep=",", encoding="utf-8")


database = DataBase(df_amazon_prime, df_netflix)

dataframe = database.transform_data()

app = FastAPI()


@app.get("/top10actors")
async def top_10_actors():
    return get_top_10_actores(dataframe)


@app.get("/top5countrys")
async def top_5_countrys():
    return get_top_5_paises(dataframe)


@app.get("/listgenres")
async def genre_moves():
    return get_list_genre_movies(dataframe)
