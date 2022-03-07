import pandas as pd
import matplotlib.pyplot as plt


def getcolumnswithdatamissing(df_data, threshold):
    return df_data[df_data.columns[df_data.isnull().mean() > threshold]].columns


def dropcolumnstesttrain(df_train, df_test, columns):
    return df_train.drop(columns=columns), df_test.drop(columns=columns)


def plotobservationpercentage(obs_percent, variable):
    obs_percent.plot(kind="bar", rot=0, xlabel=f'{variable}', ylabel="Percent",
                     title=f"Percentage of kinds of {variable} used")
    plt.show()



def observationpercentagetodrop(df_train, variable, threshold):
    obs_count = df_train[f'{variable}'].value_counts()
    obs_percent = obs_count.apply(lambda x: x/obs_count.sum()).sort_values(ascending=False)
    #plotobservationpercentage(obs_percent, variable)
    print(obs_percent[0])
    if obs_percent.values[0] > threshold:
        print("To drop")
        return False
    print("Not to drop")
    return True
