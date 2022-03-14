from Functions import *

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_all = pd.read_csv("Data/all_V0.csv", index_col=0)

# print(df_all.describe())
# print(df_all.info())
# print(df_all.corr())
# print(df_all.head())

# Merging some data

# 1stFlrSF + 2ndFlrSF  = 1stand2ndFlrSF

df_all['1stand2ndFlrSF'] = df_all['1stFlrSF'] + df_all['2ndFlrSF']

df_all.drop(columns=['1stFlrSF', '2ndFlrSF'], inplace=True)

# That makes GrLivArea nearly equal to new created variable. This is why '1stand2ndFlrSF' is dropped.

df_all.drop(columns=['1stand2ndFlrSF'], inplace=True)

# Dealing with missing values

# LotFrontage has moderate-level correlation with MSSubClass(-0.41) and LotArea(0.48). Decided to use regression model
# to predict it.

fill_reg = df_all[['MSSubClass', 'LotArea', 'LotFrontage']].dropna()
model = getlinearregressionmodel(fill_reg, ['MSSubClass', 'LotArea'], 'LotFrontage')
nans = df_all[['MSSubClass', 'LotArea', 'LotFrontage']][np.isnan(df_all['LotFrontage'])]
new_values = model.predict(nans[['MSSubClass', 'LotArea']])
df_all.loc[np.isnan(df_all['LotFrontage']), 'LotFrontage'] = new_values

# MSZoning

df_all['MSZoning'].fillna(df_all['MSZoning'].mode()[0], inplace=True)

# Exterior1st and Exterior2nd

print(df_all.loc[df_all[['Exterior1st', 'Exterior2nd']].isnull().all(axis=1)])

print(df_all.loc[(df_all['MSSubClass'] == 30) & ((df_all['YearBuilt'] >= 1936) & (df_all['YearBuilt'] <= 1944)) &
                 (df_all['ExterQual'] == 'TA') & (df_all['MasVnrType'] == 'None')].
      groupby(['Exterior1st'])['Exterior1st'].count().sort_values(ascending=False))

print(df_all.loc[(df_all['MSSubClass'] == 30) & ((df_all['YearBuilt'] >= 1936) & (df_all['YearBuilt'] <= 1944)) &
                 (df_all['ExterQual'] == 'TA') & (df_all['MasVnrType'] == 'None')].
      groupby(['Exterior2nd'])['Exterior2nd'].count().sort_values(ascending=False))

print(len(df_all.loc[df_all['Exterior1st'] == df_all['Exterior2nd']]))

# In order to fill null with most likely value it was checked what values the searched variables take for other
# features values
# Decided to replace Exterior1s and Exterior2nd with Wd Sdng.

df_all['Exterior1st'] = df_all['Exterior1st'].fillna(value='Wd Sdng')
df_all['Exterior2nd'] = df_all['Exterior2nd'].fillna(value='MetalSd')

# MasVnrType
print(df_all.loc[df_all[['MasVnrType']].isnull().all(axis=1)].head(30))

df_all = fillmissingvalues(df_all, ['Foundation', 'OverallQual', 'YearBuilt'], 'MasVnrType', [1, 2, 1])

# MasVnrArea has moderate-level correlation with OverallQual(0.43), GrLivArea(0.40) and TotalBsmtSF(0.39).
# Decided to use regression model to predict it.

fill_reg = df_all[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'MasVnrArea']].dropna()
model = getlinearregressionmodel(fill_reg, ['OverallQual', 'GrLivArea', 'TotalBsmtSF'], 'MasVnrArea')
nans = df_all[['OverallQual', 'GrLivArea', 'TotalBsmtSF', 'MasVnrArea']][np.isnan(df_all['MasVnrArea'])]
new_values = model.predict(nans[['OverallQual', 'GrLivArea', 'TotalBsmtSF']])
df_all.loc[np.isnan(df_all['MasVnrArea']), 'MasVnrArea'] = new_values

# There is one row where  all BsmtQual, BsmtExposure, BsmtFinType1, BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF
# have NULLs. Cant drop this row because it belongs to test data.

print(df_all.loc[df_all[['TotalBsmtSF']].isnull().all(axis=1)].head(30))


# BsmtQual, BsmtExposure, BsmtFinType1 replaced with none where there is a NULL in common rows

print(df_all[df_all[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1)])

nans = df_all.loc[df_all[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
                    ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']]
nans = nans.fillna('None')
df_all.loc[df_all[['BsmtQual', 'BsmtExposure', 'BsmtFinType1']].isnull().all(axis=1),
             ['BsmtQual', 'BsmtExposure', 'BsmtFinType1']] = nans

# BsmtQual

print(df_all[df_all[['BsmtQual']].isnull().all(axis=1)])

print(df_all.loc[(df_all['BsmtExposure'] == 'No')].groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False))
print(df_all.loc[(df_all['YearBuilt'] <= 1915)].groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False))
print(df_all.loc[(df_all['YearBuilt'] <= 1915) & (df_all['Foundation'] == 'Stone')].
      groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False))
print(df_all.loc[(df_all['YearBuilt'] <= 1915) & (df_all['Foundation'] == 'PConc')].
      groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False))

df_all = fillmissingvalues(df_all, ['Foundation', 'YearBuilt', 'BsmtExposure', 'BsmtFinType1'], 'BsmtQual',
                           [1.3, 1.3, 1, 1])

# BsmtExposure

df_all = fillmissingvalues(df_all, ['Foundation', 'YearBuilt', 'BsmtQual', 'BsmtFinType1'], 'BsmtExposure',
                           [1.0, 1.3, 1, 1])

#BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF

df_all[['BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF']] = df_all[['BsmtFinSF1', 'BsmtFinSF2',
                                                                           'BsmtUnfSF', 'TotalBsmtSF']].fillna(0)

# BsmtFullBath and BsmtHalfBath

print(df_all.loc[df_all[['BsmtFullBath', 'BsmtHalfBath']].isnull().all(axis=1)])

df_all = fillmissingvalues(df_all, ['BsmtQual', 'YearBuilt', 'BsmtExposure', 'BsmtFinType1'], 'BsmtFullBath',
                           [1.0, 1.0, 1, 1])
df_all = fillmissingvalues(df_all, ['BsmtQual', 'YearBuilt', 'BsmtExposure', 'BsmtFinType1'], 'BsmtHalfBath',
                           [1.0, 1.0, 1, 1])

# KitchenQual

df_all = fillmissingvalues(df_all, ['YearBuilt', 'OverallQual', 'YearRemodAdd'], 'KitchenQual', [1.0, 1, 1])

# FireplaceQu - Replacing with None

nans = df_all.loc[df_all['FireplaceQu'].isnull(), 'FireplaceQu']
nans = nans.fillna('None')
df_all.loc[df_all['FireplaceQu'].isnull(), 'FireplaceQu'] = nans

# GarageType

print(df_all.loc[(df_all[['GarageType']].isnull().all(axis=1)) & (df_all['GarageArea'] == 0.0)])

nans = df_all.loc[df_all['GarageType'].isnull(), 'GarageType']
nans = nans.fillna('None')
df_all.loc[df_all['GarageType'].isnull(), 'GarageType'] = nans

# GarageFinish

nans = df_all.loc[df_all['GarageFinish'].isnull(), 'GarageFinish']
nans = nans.fillna('None')
df_all.loc[df_all['GarageFinish'].isnull(), 'GarageFinish'] = nans


# GarageYrBlt - Can;t put a value responsible for lack of garage. Decided to drop this variable.

df_all = df_all.drop(columns=['GarageYrBlt'])

# Garage Area - linear regresssion

fill_reg = df_all[['YearBuilt', 'OverallQual', 'GarageArea', 'TotalBsmtSF', 'GrLivArea']].dropna()
model = getlinearregressionmodel(fill_reg, ['YearBuilt', 'OverallQual', 'TotalBsmtSF', 'GrLivArea'], 'GarageArea')
nans = df_all[['YearBuilt', 'OverallQual', 'GarageArea', 'TotalBsmtSF', 'GrLivArea']][np.isnan(df_all['GarageArea'])]
new_values = model.predict(nans[['YearBuilt', 'OverallQual', 'TotalBsmtSF', 'GrLivArea']])
df_all.loc[np.isnan(df_all['GarageArea']), 'GarageArea'] = new_values


# GarageCars - linear regresssion

fill_reg = df_all[['GarageArea', 'GarageCars']].dropna()
model = getlinearregressionmodel(fill_reg, ['GarageArea'], 'GarageCars')
nans = df_all[['GarageArea', 'GarageCars']][np.isnan(df_all['GarageCars'])]
new_values = model.predict(nans[['GarageArea']])
df_all.loc[np.isnan(df_all['GarageCars']), 'GarageCars'] = new_values

df_all['GarageCars'] = df_all['GarageCars'].apply(lambda x: int(x))


print(df_all.info())
print(df_all.corr() > 0.85)

# Correlation

# Decided to drop GarageCars because is correlated with GarageArea
df_all = df_all.drop(columns=['GarageCars'])

# Some of numerical data are categorical. It requires a change of type.

df_all['OverallQual'] = df_all['OverallQual'].astype('object')
df_all['OverallCond'] = df_all['OverallCond'].astype('object')
df_all['MSSubClass'] = df_all['MSSubClass'].astype('object')
df_all['YearBuilt'] = df_all['YearBuilt'].astype('object')
df_all['YearRemodAdd'] = df_all['YearRemodAdd'].astype('object')
df_all['FullBath'] = df_all['FullBath'].astype('object')
df_all['HalfBath'] = df_all['FullBath'].astype('object')
df_all['BedroomAbvGr'] = df_all['BedroomAbvGr'].astype('object')
df_all['KitchenAbvGr'] = df_all['KitchenAbvGr'].astype('object')
df_all['TotRmsAbvGrd'] = df_all['TotRmsAbvGrd'].astype('object')
df_all['Fireplaces'] = df_all['Fireplaces'].astype('object')
# df_all['GarageCars'] = df_all['GarageCars'].astype('object')
df_all['MoSold'] = df_all['MoSold'].astype('object')
df_all['YrSold'] = df_all['YrSold'].astype('object')
# df_all['GarageYrBlt'] = df_all['GarageYrBlt'].astype('object')
df_all['BsmtFullBath'] = df_all['BsmtFullBath'].astype('object')
df_all['BsmtHalfBath'] = df_all['BsmtHalfBath'].astype('object')



# Skewness operations

print(df_all.drop(columns=['SalePrice']).select_dtypes(include=np.number).skew())

columns = df_all.drop(columns=['SalePrice']).select_dtypes(include=np.number).columns

df_help = skewnesshandling(df_all.drop(columns=['SalePrice']).select_dtypes(include=np.number))

df_all = df_all.drop(columns=columns)
df_all = df_all.merge(df_help, left_index=True, right_index=True)



print(df_all.info())
# print(df_all.corr() > 0.85)
# print(df_all.corr())

# Saving data
df_all.to_csv('Data/all_V1.csv', index=True)









