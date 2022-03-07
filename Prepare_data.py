from Functions import *


pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V1.csv", index_col=0)
df_test = pd.read_csv("Data/test_V1.csv", index_col=0)

# print(df_train.info())
# print(df_test.info())

# Continuing work with categorical data
print(df_train.select_dtypes('object').info())
print(df_test.select_dtypes('object').info())
# print(df_train.select_dtypes('object').describe())


# LotShape
print(df_train['LotShape'].unique())
calculateobspercentage(df_train, 'LotShape')
boxplotxy(df_train, 'LotShape', 'SalePrice')
# Decided to connect all Irregular shapes into one

toreplace = ['IR1', 'IR2', 'IR3']
replaceobserwations(df_train, df_test, 'LotShape', toreplace, 'IR')
print(df_train['LotShape'].unique())
boxplotxy(df_train, 'LotShape', 'SalePrice')

# LotConfig

print(df_train['LotConfig'].unique())
calculateobspercentage(df_train, 'LotConfig')
boxplotxy(df_train, 'LotConfig', 'SalePrice')
# Decided to create 'other' observation for three less popular ones

toreplace = ['CulDSac', 'FR2', 'FR3']
replaceobserwations(df_train, df_test, 'LotConfig', toreplace, 'Other')
print(df_train['LotConfig'].unique())
boxplotxy(df_train, 'LotConfig', 'SalePrice')


# Neighborhood

print(df_train['Neighborhood'].unique())
calculateobspercentage(df_train, 'Neighborhood')
boxplotxy(df_train, 'Neighborhood', 'SalePrice')
# Decided to create 'other' observation for eight less popular ones

toreplace = ['ClearCr', 'StoneBr', 'SWISU', 'MeadowV', 'Blmngtn', 'BrDale', 'Veenker', 'NPkVill', 'Blueste']
replaceobserwations(df_train, df_test, 'Neighborhood', toreplace, 'Other')
print(df_train['Neighborhood'].unique())
calculateobspercentage(df_train, 'Neighborhood')
boxplotxy(df_train, 'Neighborhood', 'SalePrice')

# HouseStyle

print(df_train['HouseStyle'].unique())
calculateobspercentage(df_train, 'HouseStyle')
boxplotxy(df_train, 'HouseStyle', 'SalePrice')
# Decided to create 'other' observation for three less popular ones
toreplace = ['1.5Fin', 'SLvl', 'SFoyer', '1.5Unf', '2.5Unf', '2.5Fin']
replaceobserwations(df_train, df_test, 'HouseStyle', toreplace, 'Other')
print(df_train['HouseStyle'].unique())
boxplotxy(df_train, 'HouseStyle', 'SalePrice')


# Exterior1st
print(df_train['Exterior1st'].unique())
calculateobspercentage(df_train, 'Exterior1st')
boxplotxy(df_train, 'Exterior1st', 'SalePrice')
# Decided to create 'other' observation for eight less popular ones

toreplace = ['CBlock', 'ImStucc', 'AsphShn', 'Stone', 'BrkComm', 'AsbShng', 'Stucco', 'WdShing']
replaceobserwations(df_train, df_test, 'Exterior1st', toreplace, 'Other')
print(df_train['Exterior1st'].unique())
boxplotxy(df_train, 'Exterior1st', 'SalePrice')


# Exterior2nd
print(df_train['Exterior2nd'].unique())
calculateobspercentage(df_train, 'Exterior2nd')
boxplotxy(df_train, 'Exterior2nd', 'SalePrice')
# Decided to create 'Other' observation for nine less popular ones

toreplace = ['CBlock', 'AsphShn', 'Stone', 'Brk Cmn', 'ImStucc', 'AsbShng', 'BrkFace', 'Stucco']
replaceobserwations(df_train, df_test, 'Exterior2nd', toreplace, 'Other')
print(df_train['Exterior2nd'].unique())
boxplotxy(df_train, 'Exterior2nd', 'SalePrice')


# MasVnrType
print(df_train['MasVnrType'].unique())
calculateobspercentage(df_train, 'MasVnrType')
boxplotxy(df_train, 'MasVnrType', 'SalePrice')
# Decided to create 'Other' observation for two less popular ones

toreplace = ['BrkCmn', 'Stone']
replaceobserwations(df_train, df_test, 'MasVnrType', toreplace, 'Other')
print(df_train['MasVnrType'].unique())
boxplotxy(df_train, 'MasVnrType', 'SalePrice')


# ExterQual
print(df_train['ExterQual'].unique())
calculateobspercentage(df_train, 'ExterQual')
boxplotxy(df_train, 'ExterQual', 'SalePrice')
# Decided to create 'Other' observation for two less popular ones

toreplace = ['Fa', 'Ex']
replaceobserwations(df_train, df_test, 'ExterQual', toreplace, 'Other')
print(df_train['ExterQual'].unique())
boxplotxy(df_train, 'ExterQual', 'SalePrice')


# Foundation
print(df_train['Foundation'].unique())
calculateobspercentage(df_train, 'Foundation')
boxplotxy(df_train, 'Foundation', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['Wood', 'Stone', 'Slab']
replaceobserwations(df_train, df_test, 'Foundation', toreplace, 'Other')
print(df_train['Foundation'].unique())
boxplotxy(df_train, 'Foundation', 'SalePrice')


# BsmtQual
print(df_train['BsmtQual'].unique())
calculateobspercentage(df_train, 'BsmtQual')
boxplotxy(df_train, 'BsmtQual', 'SalePrice')
# Decided to not to combine any variables


# BsmtExposure
print(df_train['BsmtExposure'].unique())
calculateobspercentage(df_train, 'BsmtExposure')
boxplotxy(df_train, 'BsmtExposure', 'SalePrice')
# Decided to not to combine any variables

# BsmtFinType1
print(df_train['BsmtFinType1'].unique())
calculateobspercentage(df_train, 'BsmtFinType1')
boxplotxy(df_train, 'BsmtFinType1', 'SalePrice')
# Decided to not to combine any variables

# HeatingQC
print(df_train['HeatingQC'].unique())
calculateobspercentage(df_train, 'HeatingQC')
boxplotxy(df_train, 'HeatingQC', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['Po', 'Fa']
replaceobserwations(df_train, df_test, 'HeatingQC', toreplace, 'Other')
print(df_train['HeatingQC'].unique())
boxplotxy(df_train, 'HeatingQC', 'SalePrice')

# KitchenQual
print(df_train['KitchenQual'].unique())
calculateobspercentage(df_train, 'KitchenQual')
boxplotxy(df_train, 'KitchenQual', 'SalePrice')
# Decided to not to combine any variables

# FireplaceQu
print(df_train['FireplaceQu'].unique())
calculateobspercentage(df_train, 'FireplaceQu')
boxplotxy(df_train, 'FireplaceQu', 'SalePrice')
# Decided to not to combine any variables

# GarageType
print(df_train['GarageType'].unique())
calculateobspercentage(df_train, 'GarageType')
boxplotxy(df_train, 'GarageType', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['2Types', 'CarPort', 'Basment']
replaceobserwations(df_train, df_test, 'GarageType', toreplace, 'Other')
print(df_train['GarageType'].unique())
boxplotxy(df_train, 'GarageType', 'SalePrice')

# GarageFinish
print(df_train['GarageFinish'].unique())
calculateobspercentage(df_train, 'GarageFinish')
boxplotxy(df_train, 'GarageFinish', 'SalePrice')
# Decided to not to combine any variables