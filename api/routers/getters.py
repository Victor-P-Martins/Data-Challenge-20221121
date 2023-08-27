import pandas as pd
from pandas import DataFrame


def get_top_10_actores(dataframe: DataFrame) -> dict:
    df_compare_country_company = (
        dataframe.groupby(by=["cast_list"])["show_id"]
        .count()
        .reset_index()
        .sort_values("show_id", ascending=False)
        .rename(columns={"show_id": "count"})
    )
    df_compare_country_company = df_compare_country_company.rename(
        columns={"cast_list": "ator"}
    )

    return df_compare_country_company.head(10).to_dict(orient="index")


def get_top_5_paises(dataframe: DataFrame) -> dict:
    df_compare_country_company = (
        dataframe.groupby(by=["company", "country_list"])["show_id"]
        .count()
        .reset_index()
        .sort_values("show_id", ascending=False)
        .rename(columns={"show_id": "count"})
    )
    dict_netflix = (
        df_compare_country_company[df_compare_country_company["company"] == "Netflix"]
        .head(5)
        .to_dict(orient="index")
    )
    dict_prime = (
        df_compare_country_company[df_compare_country_company["company"] == "Prime"]
        .head(5)
        .to_dict(orient="index")
    )

    return dict_netflix | dict_prime


def get_list_genre_movies(dataframe: DataFrame) -> list:
    return dataframe["listed_in"].str.split(", ").explode().unique().tolist()
