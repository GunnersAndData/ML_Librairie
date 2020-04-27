import pandas as pd
import numpy as np
from typing import Union
from sklearn.impute import SimpleImputer


# Select a kind of features
# kind : [number,int,float64,category,datetimetz]
def selectKindFeatures(df: pd.DataFrame,
                       kind: Union[None,str] = 'number') -> Union[str, pd.DataFrame]:
    if len(df.select_dtypes(include=kind).columns) == 0:
        return f"Le dataframe ne contient pas de variables du type {kind}"
    return df.select_dtypes(include=kind)


def fillna(df: pd.DataFrame,
           col_to_fill: pd.Series,
           missing_values: Union[str, float, int],
           strategy: str,
           inplace: bool = False):
    imp = SimpleImputer(missing_values=missing_values, strategy=strategy)
    if inplace:
        df[col_to_fill] = imp.fit_transform(df[[col_to_fill]]).ravel()
    return imp.fit_transform(df[[col_to_fill]]).ravel()