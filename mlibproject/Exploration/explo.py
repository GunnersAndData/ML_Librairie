import pandas as pd


def missing_Values(df: pd.DataFrame):
    print("NaN in each columns ", df.isnull().sum().sort_values(ascending=False), sep='\n')


def shape(df: pd.DataFrame) -> str:
    return f"le jeu de données a : {df.shape[0]} lignes et {df.shape[1]} colonnes"


def describeT(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include='all').T
