from Functions import *
from sklearn.impute import KNNImputer

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V2.csv", index_col=0)
df_test = pd.read_csv("Data/test_V2.csv", index_col=0)
print(df_train.describe())
print(df_train.info())
print(df_test.info())
print(df_train.corr()[df_train.corr() > 0.8])
print(df_train.head())

# Dealing with missing values

# LotFrontage is average level correlated with 1stFlrSF and  GrLivArea and LotArea

fill_reg = df_train[['1stFlrSF', 'GrLivArea', 'LotArea', 'LotFrontage']].dropna()
model = getlinearregressionmodel(fill_reg, ['1stFlrSF', 'GrLivArea', 'LotArea'], 'LotFrontage')
nans = df_train[['1stFlrSF', 'GrLivArea', 'LotArea', 'LotFrontage']][np.isnan(df_train['LotFrontage'])]
new_values = model.predict(nans[['1stFlrSF', 'GrLivArea', 'LotArea']])
df_train.loc[np.isnan(df_train['LotFrontage']), 'LotFrontage'] = new_values
nans = df_test[['1stFlrSF', 'GrLivArea', 'LotArea', 'LotFrontage']][np.isnan(df_test['LotFrontage'])]
new_values = model.predict(nans[['1stFlrSF', 'GrLivArea', 'LotArea']])
df_test.loc[np.isnan(df_test['LotFrontage']), 'LotFrontage'] = new_values


# GarageType, GarageFinish and GarageYrBlt have nulls in the same rows. it means that there is no garage next to house.
# Decided to replace Null values with "None"
df_train, df_test = dropcolumnstesttrain(df_train, df_test, ['GarageYrBlt'])
nans = df_train.loc[df_train[['GarageType', 'GarageFinish']].isnull().all(axis=1), ['GarageType', 'GarageFinish']]
nans = nans.fillna('None')
df_train.loc[df_train[['GarageType', 'GarageFinish']].isnull().all(axis=1), ['GarageType', 'GarageFinish']] = nans
nans = df_test.loc[df_test[['GarageType', 'GarageFinish']].isnull().all(axis=1), ['GarageType', 'GarageFinish']]
nans = nans.fillna('None')
df_test.loc[df_test[['GarageType', 'GarageFinish']].isnull().all(axis=1), ['GarageType', 'GarageFinish']] = nans
# GarageYrBlt is tricky one. As it is correlated with rear build
# (Most of garages was build in the same year like whole house). Gonna work with it later
# FireplaceQu - Replacing with None

nans = df_train.loc[df_train['FireplaceQu'].isnull(), 'FireplaceQu']
nans = nans.fillna('None')
df_train.loc[df_train['FireplaceQu'].isnull(), 'FireplaceQu'] = nans
nans = df_test.loc[df_test['FireplaceQu'].isnull(), 'FireplaceQu']
nans = nans.fillna('None')
df_test.loc[df_test['FireplaceQu'].isnull(), 'FireplaceQu'] = nans

#'BsmtQual, BsmtExposure, BsmtFinType1 replaced with none where there is a NULL in common rows

# print(df_train[df_train[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1)])

nans = df_train.loc[df_train[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
                    ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']]
nans = nans.fillna('None')
df_train.loc[df_train[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
             ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']] = nans
nans = df_test.loc[df_test[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
                   ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']]
nans = nans.fillna('None')
df_test.loc[df_test[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
            ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']] = nans

# Single rows with nulls without any known NULL trend. Exterior1s and Exterior2nd

print(df_test.loc[df_test[['Exterior1st', 'Exterior2nd']].isnull().all(axis=1)])
print(df_test.loc[df_test['ExterQual'] == "TA"])
print(df_test.loc[df_test['ExterQual'] == "TA"].groupby(['Exterior1st'])['Exterior1st'].count().sort_values(
    ascending=False))
print(df_test.loc[df_test['YearBuilt'] == 1940].groupby(['Exterior1st'])['Exterior1st'].count().sort_values(
    ascending=False))
print(df_test.loc[df_test['ExterQual'] == "TA"].groupby(['Exterior2nd'])['Exterior2nd'].count().sort_values(
    ascending=False))
print(df_test.loc[df_test['YearBuilt'] == 1940].groupby(['Exterior2nd'])['Exterior2nd'].count().sort_values(
    ascending=False))
print(len(df_test.loc[df_test['Exterior1st'] == df_test['Exterior2nd']]))

# In order to fill null with likely value it was checked what values the searched variables take for other features.
# Decided to replace Exterior1s and Exterior2nd with Wd Sdng because this value appears in the most cases for year in
# which nulls occur. Also in nearly 90% of cases Exterior1s and Exterior2nd have the same values.

df_test[['Exterior1st', 'Exterior2nd']] = df_test[['Exterior1st', 'Exterior2nd']].fillna(value='Wd Sdng')

# MasVnrType

print(df_test.loc[df_test[['MasVnrType']].isnull().all(axis=1)].head(30))
#print(df_train.loc[df_train[['MasVnrType']].isnull().all(axis=1)].head(30))
print(df_train['MasVnrType'].value_counts())
print(df_test['MasVnrType'].value_counts())
df_train = fillmissingvalues(df_train, ['ExterQual', 'YearBuilt'], 'MasVnrType')
df_test = fillmissingvalues(df_test, ['ExterQual', 'YearBuilt'], 'MasVnrType')

# BsmtQual

print(df_test.loc[df_test[['BsmtQual', 'BsmtExposure']].isnull().any(axis=1)])
df_test = fillmissingvalues(df_test, ['Foundation', 'YearBuilt', 'BsmtExposure', 'BsmtFinType1'], 'BsmtQual')

# BsmtExposure

df_test = fillmissingvalues(df_test, ['Foundation', 'YearBuilt', 'BsmtQual', 'BsmtFinType1'], 'BsmtExposure')
df_train = fillmissingvalues(df_train, ['Foundation', 'YearBuilt', 'BsmtQual', 'BsmtFinType1'], 'BsmtExposure')

# KitchenQual

df_test = fillmissingvalues(df_test, ['YearBuilt'], 'KitchenQual')

# GarageType

print(df_test.loc[df_test[['GarageFinish']].isnull().any(axis=1)])
df_test = fillmissingvalues(df_test, ['GarageType', 'YearBuilt'], 'GarageFinish')

# BsmtFinSF1, BsmtUnfSF, TotalBsmtSF - filling NULLS with zeros as they don't have basement

print(df_test.loc[df_test[['BsmtFinSF1']].isnull().any(axis=1)])
df_test.fillna(value={'BsmtFinSF1': 0, 'BsmtUnfSF': 0, 'TotalBsmtSF': 0}, inplace=True)


# GarageArea - filling by using regression

print(df_test.loc[df_test[['GarageArea']].isnull().any(axis=1)])
print(df_test.loc[df_test['GarageFinish'] == "Unf"])

fill_reg = df_train.loc[(df_train['GarageFinish'] == "Unf") & (df_train['GarageType'] == "Detchd"),
                        ['GrLivArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt', 'GarageArea']].dropna()
model = getlinearregressionmodel(fill_reg, ['GrLivArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt'], 'GarageArea')
nans = df_test[['GrLivArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt', 'GarageArea']][np.isnan(df_test['GarageArea'])]
new_values = model.predict(nans[['GrLivArea', 'TotalBsmtSF', '1stFlrSF', 'YearBuilt']])
df_test.loc[np.isnan(df_test['GarageArea']), 'GarageArea'] = new_values


'''

fill_reg = df_train[['1stFlrSF', 'TotalBsmtSF', 'BsmtUnfSF', 'BsmtFinSF1']].dropna()
model = getlinearregressionmodel(fill_reg, ['1stFlrSF', 'TotalBsmtSF', 'BsmtUnfSF'], 'BsmtFinSF1')
nans = df_test[['1stFlrSF', 'TotalBsmtSF', 'BsmtUnfSF', 'BsmtFinSF1']][np.isnan(df_test['BsmtFinSF1'])]
new_values = model.predict(nans[['1stFlrSF', 'TotalBsmtSF', 'BsmtUnfSF']])
df_test.loc[np.isnan(df_test['BsmtFinSF1']), 'BsmtFinSF1'] = new_values
'''
print(df_test.info())
print(df_train.info())


# Saving data
df_train.to_csv('Data/train_V3.csv', index=True)
df_test.to_csv('Data/test_V3.csv', index=True)
