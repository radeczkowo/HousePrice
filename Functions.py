import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def getcolumnswithdatamissing(df_data, threshold):
    return df_data[df_data.columns[df_data.isnull().mean() > threshold]].columns


def dropcolumnstesttrain(df_train, df_test, columns):
    return df_train.drop(columns=columns), df_test.drop(columns=columns)


def plotobservationpercentage(obs_percent, variable):
    obs_percent.plot(kind="bar", rot=0, xlabel=f'{variable}', ylabel="Percent",
                     title=f"Percentage of kinds of {variable} used")
    plt.show()


def calculateobspercentage(df_train, variable):
    obs_count = df_train[f'{variable}'].value_counts()
    obs_percent = obs_count.apply(lambda x: x/obs_count.sum()).sort_values(ascending=False)
    print(obs_percent)
    plotobservationpercentage(obs_percent, variable)
    return obs_percent



def observationpercentagetodrop(df_train, variable, threshold):
    obs_percent = calculateobspercentage(df_train, variable)
    #print(obs_percent[0])
    if obs_percent.values[0] > threshold:
        #print("To drop")
        return False
    #print("Not to drop")
    return True

def boxplotxy(df_train, x, y):
    Xy_group = df_train.groupby(x)[y].mean().sort_values(ascending=False)
    print(Xy_group)
    Xy_group.plot(kind="bar", rot=0, xlabel=x, ylabel=f"Average {y}", title=f"Average {y} by {x}")
    plt.show()


def replaceobserwations(df_train, df_test, column, toreplace, replacement):
    df_train[column] = df_train[column].replace(toreplace, replacement)
    df_test[column] = df_test[column].replace(toreplace, replacement)

