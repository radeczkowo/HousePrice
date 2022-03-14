from Functions import *
from sklearn.preprocessing import MinMaxScaler

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V4.csv", index_col=0)
df_test = pd.read_csv("Data/test_V4.csv", index_col=0)

print(df_train.info())
print(df_test.info())
print(df_train.corr())

df_train['SalePrice'] = np.log1p(df_train['SalePrice'])
df_train['SalePrice'] = df_train['SalePrice'].apply(lambda x: int(x))

# Using Extra Trees Classifier feature importance for dropping some less useful variables
df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 3)
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getnoimportantvar(df_var_import, 0.03))


# Using Extra Trees Classifier feature importance to clarify final variables
df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 3)
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getnoimportantvar(df_var_import, 0.075))

df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 3)



print(df_train.info())
# print(df_test.info())
# print(df_train.head())

for var in df_train.columns:
    plt.scatter(df_train[var], df_train['SalePrice'])
    plt.xlabel(var)
    plt.ylabel("SalePrice")
    # plt.show()

print(df_train.loc[(df_train['GrLivArea'] > 8.2), ['SalePrice', 'GrLivArea']])
print(df_train.loc[(df_train['Neighborhood'] == 4) & (df_train['SalePrice'] == 13), ['SalePrice', 'Neighborhood']])
df_train = df_train.drop([524, 1299])
# Saving data
df_train.to_csv('Data/train_V5.csv', index=True)
df_test.to_csv('Data/test_V5.csv', index=True)