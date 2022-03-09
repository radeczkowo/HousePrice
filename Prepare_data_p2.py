from Functions import *

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V2.csv", index_col=0)
df_test = pd.read_csv("Data/test_V2.csv", index_col=0)
# print(df_train.info())
# print(df_test.info())

#Dealing with missing values

# Both GarageType and GarageFinish have nulls in the same rows. it means that there is no garage next to house.
# Decided to replace Null values with "None"
nans = df_train.loc[df_train[['GarageType', 'GarageFinish']].isnull().any(axis=1), ['GarageType', 'GarageFinish']]
nans = nans.fillna('None')
df_train.loc[df_train[['GarageType', 'GarageFinish']].isnull().any(axis=1), ['GarageType', 'GarageFinish']] = nans
nans = df_test.loc[df_test[['GarageType', 'GarageFinish']].isnull().any(axis=1), ['GarageType', 'GarageFinish']]
nans = nans.fillna('None')
df_test.loc[df_test[['GarageType', 'GarageFinish']].isnull().any(axis=1), ['GarageType', 'GarageFinish']] = nans

# Nulls in variable "GarageFinish" occur in the same rows as in above mentioned features.

print(df_train.info())
print(df_test.info())

# Saving data
df_train.to_csv('Data/train_V3.csv', index=False)
df_test.to_csv('Data/test_V3.csv', index=False)