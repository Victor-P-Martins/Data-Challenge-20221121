import pandas as pd
from pandas import DataFrame


class DataBase:
    def __init__(
        self, dataframe_prime: DataFrame, dataframe_netflix: DataFrame
    ) -> None:
        self.dataframe_prime = dataframe_prime
        self.dataframe_netflix = dataframe_netflix

    def __create_merged_dataframe(
        self, dataframe_prime, dataframe_netflix
    ) -> DataFrame:
        dataframe_prime["company"] = "Prime"
        dataframe_netflix["company"] = "Netflix"

        df_total_companys = pd.concat(
            [self.dataframe_prime, self.dataframe_netflix], ignore_index=True
        )
        return df_total_companys

    def __transform_country_column(self, dataframe) -> DataFrame:
        df_total_companys = dataframe

        df_total_companys["country_list"] = df_total_companys["country"].str.split(",")
        df_total_companys = df_total_companys.explode(["country_list"])

        df_total_companys = df_total_companys.dropna(subset=["country_list"])

        df_total_companys["country_list"] = df_total_companys[
            "country_list"
        ].str.strip()

        return df_total_companys

    def __transform_cast_column(self, dataframe) -> DataFrame:
        df_total_companys = dataframe
        df_total_companys["cast_list"] = df_total_companys["cast"].str.split(",")
        df_total_companys = df_total_companys.explode(["cast_list"])
        df_total_companys = df_total_companys.dropna(subset=["cast_list"])

        df_total_companys["cast_list"] = df_total_companys["cast_list"].str.strip()

        return df_total_companys

    def __transform_date_column(self, dataframe) -> DataFrame:
        df_total_companys = dataframe

        df_total_companys["year_added"] = df_total_companys["date_added"].str.split(
            ",", expand=True
        )[1]
        df_total_companys["month_added"] = (
            df_total_companys["date_added"]
            .str.split(",", expand=True)[0]
            .str.split(" ", expand=True)[0]
        )

        return df_total_companys

    def transform_data(self) -> DataFrame:
        dataframe = self.__create_merged_dataframe(
            self.dataframe_prime, self.dataframe_netflix
        )
        dataframe = self.__transform_country_column(dataframe)
        dataframe = self.__transform_cast_column(dataframe)
        dataframe = self.__transform_date_column(dataframe)

        return dataframe


if __name__ == "__main__":
    df_amazon_prime = pd.read_csv(
        r"api\data\amazon_prime_titles.csv", sep=",", encoding="utf-8"
    )
    df_netflix = pd.read_csv(r"api\data\netflix_titles.csv", sep=",", encoding="utf-8")

    database = DataBase(df_amazon_prime, df_netflix)

    df = database.transform_data()

    df.columns

    df_compare_country_company = (
        df.groupby(by=["cast_list"])["show_id"]
        .count()
        .reset_index()
        .sort_values("show_id", ascending=False)
        .rename(columns={"show_id": "count"})
    )
    df_compare_country_company = df_compare_country_company.rename(
        columns={"cast_list": "Ator"}
    )

    df_compare_country_company.head(10).to_dict(orient="index")

    df_compare_country_company.to_json()

    import json

    print(json.dumps(df_compare_country_company.head(10).to_dict()))
