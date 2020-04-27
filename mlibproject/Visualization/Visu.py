import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Union
sns.set()


# Distribution
def display_distribution(df: pd.DataFrame,
                         numerical_cols: list):

    plt.figure(figsize=(20, 8))
    i = 0
    for column_ in numerical_cols:
        i = i + 1
        plt.subplot(2, 2, i)
        sns.distplot(df[column_], label='Data', hist=False)
        plt.legend()
        plt.xlabel(numerical_cols[i-1], fontsize=12)

    plt.show()


# Correlation matrix
def corr_matrix(df: pd.DataFrame,
                statistique_test: Union[None,str] = 'pearson'):
    plt.figure(figsize=(10,10))
    sns.heatmap(df.corr(statistique_test),
                cmap=plt.cm.RdBu,
                vmax=1.0,
                linewidths=0.1,
                linecolor='white',
                square=True,
                annot=True
                )


def pair_plot(df: pd.DataFrame,
              numerical_cols: list,
              stacked_col: Union[None, str] = None):
    plt.figure(figsize=(10, 10))
    if stacked_col is not None:
        numerical_cols.append(stacked_col)
        sns.pairplot(df[numerical_cols], height=2, hue=stacked_col)
    else:
        sns.pairplot(df[numerical_cols], height=2)


# Boxplot
def display_boxplot(df: pd.DataFrame,
                    numerical_cols: list):
    plt.figure(figsize=(20,8))
    i = 0
    for columns_ in numerical_cols:
        i = i+1
        plt.subplot(2, 2, i)
        sns.boxplot(x=df[columns_], data=df, palette='viridis')


# stacked Boxplot
def display_stackedboxplot(df: pd.DataFrame,
                           numerical_cols: list,
                           target: str):
    plt.figure(figsize=(20,8))
    i = 0
    for columns_ in numerical_cols:
        i = i+1
        plt.subplot(2, 2, i)
        sns.boxplot(x=df[target], y=df[columns_], data=df, palette="viridis")


if __name__ == '__main__':
    import os
    data = pd.read_csv(os.path.join(os.getcwd(), 'churn.csv'), encoding='utf-8')
    print(data.head())
    display_stackedboxplot(data, numerical_cols= ['MonthlyCharges'],target='Churn')