from Functions import *

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V1.csv", index_col=0)
df_test = pd.read_csv("Data/test_V1.csv", index_col=0)

# Using Extra trees classifier to drop some numeric features, which importance is too low for prediction
print(df_train.select_dtypes(include=np.number).info())

df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 4)
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getnoimportantvar(df_var_import, 0.02))
df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 4)
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getnoimportantvar(df_var_import, 0.04))
df_var_import = extratreefeatureselection(df_train.select_dtypes(include=np.number), 'SalePrice', 1)
print(df_train.select_dtypes(include=np.number).info())

# Saving data
df_train.to_csv('Data/train_V2.csv', index=False)
df_test.to_csv('Data/test_V2.csv', index=False)








