import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
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
              target: Union[None,str] = None):
    plt.figure(figsize=(10, 10))
    if target is not None:
        numerical_cols.append(target)
        sns.pairplot(df[numerical_cols],height=2, hue=target)
    else:
        sns.pairplot(df[numerical_cols],height=2)


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


def display_scatterPlotlyTarget(df: pd.DataFrame, col_x: str,
                                col_y: str, Path: Union[None, str] = str(os.getcwd()),
                                save: bool = False):
    assert (len(df[
                    col_y].unique())) == 2, 'target with cardinality equal 2 is required'
    col_y_bool = col_y + "_bool"
    fig_title = f"{col_x} in terms of {col_y} Rate"
    df[col_y_bool] = np.where(df[col_y] == "No", 0, 1)
    df_grouped = df.groupby(col_x)[col_y_bool].mean().reset_index()
    plot_data = px.scatter(x=df_grouped[col_x],
                           y=df_grouped[col_y_bool],
                           title=fig_title)
    plot_data.update_layout(xaxis=dict(title_text=f'{col_x}'),
                            yaxis=dict(title_text=f'{col_y}_rate'))

    plot_data.show()

    if save == True and Path is not None:
        figname = fig_title.replace(" ", "_")
        plot_data.write_image(f"{Path}/{figname}.png")


def display_stackedBarplotPlotly(df: pd.DataFrame, col_x: str,
                                 col_y: str, save: bool = False,
                                 Path: Union[None, str] = str(os.getcwd())):
    assert (len(df[
                    col_y].unique())) == 2, 'at least target with cardinality equal 2 is required'
    col_y_bool = col_y + "_bool"
    fig_title = f"{col_x} in terms of {col_y} Rate"
    df[col_y_bool] = np.where(df[col_y] == "No", 0, 1)
    df_grouped = df.groupby(col_x)[col_y_bool].mean().reset_index()
    plot_data = px.bar(x=df_grouped[col_x],
                       y=df_grouped[col_y_bool],
                       color=df_grouped[col_x])

    plot_data.update_layout(xaxis=dict(title_text=f'{col_x}'),
                            yaxis=dict(title_text=f'{col_y}_rate'))

    plot_data.show()

    if save and Path is not None:
        figname = fig_title.replace(" ", "_")
        plot_data.write_image(f"{Path}/{figname}.png")