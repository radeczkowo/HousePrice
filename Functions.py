import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import linear_model
from sklearn import preprocessing
import sklearn
from scipy import stats


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
    # plotobservationpercentage(obs_percent, variable)
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
    # plt.show()


def replaceobserwations(df_train, df_test, column, toreplace, replacement):
    df_train[column] = df_train[column].replace(toreplace, replacement)
    df_test[column] = df_test[column].replace(toreplace, replacement)


def extratreefeatureselection(Xy, yname, times):
    w = pd.DataFrame(Xy.drop(columns=[yname]).columns)
    model = ExtraTreesClassifier()
    Xy = Xy[~Xy.isnull().any(axis=1)]
    print(len(Xy))
    X = Xy.drop(columns=[yname]).values
    X = preprocessing.scale(X)
    y = Xy[yname].values
    for n in range(times):
        model.fit(X, y)
        w[str(n+1)] = model.feature_importances_

    w['mean'] = w.select_dtypes(include=np.number).mean(axis=1)
    w.rename(columns={0: 'variable'}, inplace=True)
    print(w[['variable', 'mean']])
    return w[['variable', 'mean']]


def getnoimportantvar(data, value):
    return data.loc[data["mean"] < value, 'variable'].tolist()


def getlinearregressionmodel(dataframe, Xx, yy):
    X = dataframe[Xx]
    y = dataframe[yy]
    model = linear_model.LinearRegression()
    model.fit(X, y)
    return model


def mapvariable(df_train, df_test, variable, mapping):
    df_train[variable] = df_train[variable].map(mapping).astype(int)
    df_test[variable] = df_test[variable].map(mapping).astype(int)
    return df_train, df_test


def fillmissingvalues(df, columns, variable, wages):
    values = []
    df_nulls = df.loc[df[[variable]].isnull().all(axis=1)]
    df_counts = pd.DataFrame(index=df[variable].unique())
    for nr in range(len(df_nulls)):
        n = 0
        for column in columns:
            observation = df_nulls[column].iloc[nr]
            df_count = df.loc[df[column] == observation].groupby([variable])[variable].count().sort_values(
                ascending=False)
            df_count = pd.DataFrame({nr: df_count}, index=df[variable].unique())
            df_count[nr] = df_count[nr].apply(lambda x: x/df_count[nr].sum()*wages[n])
            df_counts = pd.concat([df_counts, df_count], axis=1)
            n = n + 1
        df_counts['sum'] = df_counts.sum(axis=1)
        print(df_counts['sum'].sort_values(ascending=False))
        values.append(df_counts['sum'].sort_values(ascending=False).index.values[0])
        df_counts = df_counts.drop(df_counts.columns, 1)
    df.loc[df[[variable]].isnull().all(axis=1), variable] = values
    return df

def testmodel(df_train, model, y, percent):
    df_train = sklearn.utils.shuffle(df_train)

    X = df_train.drop(columns=[y]).values
    X = preprocessing.scale(X)
    y = df_train[y].values

    length = int(percent*len(df_train))

    X_train = X[:-length]
    y_train = y[:-length]

    X_test = X[-length:]
    y_test = y[-length:]
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(model.score(X_test, y_test))
    error = np.power((y_pred-y_test), 2).sum()/len(y_test)
    print(error)
    plt.scatter(y_pred, y_test-y_pred, color="green")
    # plt.show()

def finalprediction(model, df_train, df_test, y, df_submission):
    df_train = sklearn.utils.shuffle(df_train)

    X = df_train.drop(columns=[y]).values
    X = preprocessing.scale(X)
    yy = df_train[y].values

    model.fit(X, yy)

    X_test = preprocessing.scale(df_test)
    y_pred = model.predict(X_test)
    df_submission[y] = y_pred
    df_submission[y] = df_submission[y].apply(lambda x: np.exp(x))
    df_submission.to_csv('Data/submission.csv', index=True)



def replacingoutlieriqr(variable):
    q25, q75 = np.percentile(variable, 25), np.percentile(variable, 75)
    iqr = q75 - q25
    limit = iqr * 1.5
    lower, upper = q25 - limit, q75 + limit
    variable = np.where(variable < lower, lower, variable)
    variable = np.where(variable > upper, upper, variable)
    return variable

def skewnesshandling(df_train):
    df_help = pd.DataFrame()
    print(df_train.skew())
    skewness = df_train.skew().sort_values(ascending=False)
    print(skewness)
    skewness = skewness[abs(skewness) > 1]
    for var in skewness.index:
        print(var)
        print(df_train[var].skew())
        df_train[var].plot.kde(bw_method=1)
        # plt.show()
        df_help[var] = np.log1p(df_train[var])
        print(df_help[var].skew())
        df_help[var].plot.kde(bw_method=1)
        # plt.show()
        if abs(df_help[var].skew()) > 0.75:
            df_help[var] = np.sqrt(df_train[var])
            print(df_train[var].skew())
            df_help[var].plot.kde(bw_method=1)
            # plt.show()
        else:
            df_train[var] = df_help[var]
    return df_train























