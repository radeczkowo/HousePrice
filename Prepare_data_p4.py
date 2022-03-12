from Functions import *
from sklearn.preprocessing import MinMaxScaler

# Continuing work with categorical data

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V4.csv", index_col=0)
df_test = pd.read_csv("Data/test_V4.csv", index_col=0)

# Using Extra Trees Classifier feature importance for dropping some less useful variables
df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 3)
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getnoimportantvar(df_var_import, 0.03))

print(df_train.info())
print(df_test.info())
print(df_train.corr()[df_train.corr() > 0.8])

# TotalBsmtSF and 1stFlrSF are correlated(coefficient above 0.8). Both features will be merged into one.

Scaler = MinMaxScaler()
df_train[['1stFlrSF', 'TotalBsmtSF']] = Scaler.fit_transform(df_train[['1stFlrSF', 'TotalBsmtSF']])
df_test[['1stFlrSF', 'TotalBsmtSF']] = Scaler.fit_transform(df_test[['1stFlrSF', 'TotalBsmtSF']])
df_train['1stFlrSFTotalBsmtSF'] = (df_train['1stFlrSF'] + df_train['TotalBsmtSF'])/2
df_test['1stFlrSFTotalBsmtSF'] = (df_test['1stFlrSF'] + df_train['TotalBsmtSF'])/2
df_train, df_test = dropcolumnstesttrain(df_train, df_test, ['1stFlrSF', 'TotalBsmtSF'])

print(df_train.info())
print(df_test.info())
print(df_train.corr()[df_train.corr() > 0.8])

df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 3)

# Saving data
df_train.to_csv('Data/train_V5.csv', index=True)
df_test.to_csv('Data/test_V5.csv', index=True)