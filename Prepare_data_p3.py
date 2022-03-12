from Functions import *

# Continuing work with categorical data

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V3.csv", index_col=0)
df_test = pd.read_csv("Data/test_V3.csv", index_col=0)

print(df_train.info())
print(df_test.info())


# LotShape
print(df_train['LotShape'].unique())
calculateobspercentage(df_train, 'LotShape')
boxplotxy(df_train, 'LotShape', 'SalePrice')
# Decided to connect all Irregular shapes into one

toreplace = ['IR1', 'IR2', 'IR3']
replaceobserwations(df_train, df_test, 'LotShape', toreplace, 'IR')
print(df_train['LotShape'].unique())
boxplotxy(df_train, 'LotShape', 'SalePrice')

mapping = {"Reg": 1, "IR": 2}
mapvariable(df_train, df_test, 'LotShape', mapping)

# LotConfig

print(df_train['LotConfig'].unique())
calculateobspercentage(df_train, 'LotConfig')
boxplotxy(df_train, 'LotConfig', 'SalePrice')
# Decided to create 'other' observation for three less popular ones

toreplace = ['CulDSac', 'FR2', 'FR3']
replaceobserwations(df_train, df_test, 'LotConfig', toreplace, 'Other')
print(df_train['LotConfig'].unique())
boxplotxy(df_train, 'LotConfig', 'SalePrice')

mapping = {"Inside": 1, "Corner": 2, 'Other': 3}
mapvariable(df_train, df_test, 'LotConfig', mapping)
print(df_train.info())
print(df_test.info())

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

mapping = {"IDOTRR": 1, "BrkSide": 2, 'Edwards': 3, "OldTown": 4, "Sawyer": 5, 'NAmes': 6, "Mitchel": 7, "SawyerW": 8,
           'Other': 9, "NWAmes": 10, "Gilbert": 11, 'CollgCr': 12, "Crawfor": 13, "Somerst": 14, 'Timber': 15,
           "NridgHt": 16, 'NoRidge': 17}
mapvariable(df_train, df_test, 'Neighborhood', mapping)

# HouseStyle

print(df_train['HouseStyle'].unique())
calculateobspercentage(df_train, 'HouseStyle')
boxplotxy(df_train, 'HouseStyle', 'SalePrice')
# Decided to create 'other' observation for three less popular ones
toreplace = ['1.5Fin', 'SLvl', 'SFoyer', '1.5Unf', '2.5Unf', '2.5Fin']
replaceobserwations(df_train, df_test, 'HouseStyle', toreplace, 'Other')
print(df_train['HouseStyle'].unique())
boxplotxy(df_train, 'HouseStyle', 'SalePrice')

mapping = {"Other": 1, "1Story": 2, '2Story': 3}
mapvariable(df_train, df_test, 'HouseStyle', mapping)


# Exterior1st
print(df_train['Exterior1st'].unique())
calculateobspercentage(df_train, 'Exterior1st')
boxplotxy(df_train, 'Exterior1st', 'SalePrice')
# Decided to create 'other' observation for eight less popular ones

toreplace = ['CBlock', 'ImStucc', 'AsphShn', 'Stone', 'BrkComm', 'AsbShng', 'Stucco', 'WdShing']
replaceobserwations(df_train, df_test, 'Exterior1st', toreplace, 'Other')
print(df_train['Exterior1st'].unique())
boxplotxy(df_train, 'Exterior1st', 'SalePrice')


mapping = {"Other": 1, "MetalSd": 2, 'Wd Sdng': 3, "HdBoard": 4, "Plywood": 5, 'BrkFace': 6, "VinylSd": 7, "CemntBd": 8}
mapvariable(df_train, df_test, 'Exterior1st', mapping)

print(df_train.info())
print(df_test.info())
# Exterior2nd
print(df_train['Exterior2nd'].unique())
calculateobspercentage(df_train, 'Exterior2nd')
boxplotxy(df_train, 'Exterior2nd', 'SalePrice')
# Decided to create 'Other' observation for nine less popular ones

toreplace = ['CBlock', 'AsphShn', 'Stone', 'Brk Cmn', 'ImStucc', 'AsbShng', 'BrkFace', 'Stucco']
replaceobserwations(df_train, df_test, 'Exterior2nd', toreplace, 'Other')
print(df_train['Exterior2nd'].unique())
boxplotxy(df_train, 'Exterior2nd', 'SalePrice')

print(df_train['Exterior2nd'].unique())
mapping = {"Wd Sdng": 1, "MetalSd": 2, 'Wd Shng': 3, "Other": 4, "HdBoard": 5, 'Plywood': 6, "VinylSd": 7, "CmentBd": 8}
mapvariable(df_train, df_test, 'Exterior2nd', mapping)

# MasVnrType
print(df_train['MasVnrType'].unique())
calculateobspercentage(df_train, 'MasVnrType')
boxplotxy(df_train, 'MasVnrType', 'SalePrice')
# Decided to create 'Other' observation for two less popular ones

toreplace = ['BrkCmn', 'Stone']
replaceobserwations(df_train, df_test, 'MasVnrType', toreplace, 'Other')
print(df_train['MasVnrType'].unique())
boxplotxy(df_train, 'MasVnrType', 'SalePrice')

mapping = {"None": 1, "BrkFace": 2, "Other": 3}
mapvariable(df_train, df_test, 'MasVnrType', mapping)

# ExterQual
print(df_train['ExterQual'].unique())
calculateobspercentage(df_train, 'ExterQual')
boxplotxy(df_train, 'ExterQual', 'SalePrice')
# Decided to create 'Other' observation for two less popular ones

toreplace = ['Fa', 'Ex']
replaceobserwations(df_train, df_test, 'ExterQual', toreplace, 'Other')
print(df_train['ExterQual'].unique())
boxplotxy(df_train, 'ExterQual', 'SalePrice')

mapping = {"TA": 1, "Gd": 2, "Other": 3}
mapvariable(df_train, df_test, 'ExterQual', mapping)

# Foundation
print(df_train['Foundation'].unique())
calculateobspercentage(df_train, 'Foundation')
boxplotxy(df_train, 'Foundation', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['Wood', 'Stone', 'Slab']
replaceobserwations(df_train, df_test, 'Foundation', toreplace, 'Other')
print(df_train['Foundation'].unique())
boxplotxy(df_train, 'Foundation', 'SalePrice')

mapping = {"Other": 1, "BrkTil": 2, "CBlock": 3, "PConc": 4}
mapvariable(df_train, df_test, 'Foundation', mapping)

# BsmtQual
print(df_train['BsmtQual'].unique())
calculateobspercentage(df_train, 'BsmtQual')
boxplotxy(df_train, 'BsmtQual', 'SalePrice')
# Decided to not to combine any variables

mapping = {"None": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
mapvariable(df_train, df_test, 'BsmtQual', mapping)


# BsmtExposure
print(df_train['BsmtExposure'].unique())
calculateobspercentage(df_train, 'BsmtExposure')
boxplotxy(df_train, 'BsmtExposure', 'SalePrice')
# Decided to not to combine any variables

mapping = {"None": 1, "No": 2, "Mn": 3, "Av": 4, "Gd": 5}
mapvariable(df_train, df_test, 'BsmtExposure', mapping)

# BsmtFinType1
print(df_train['BsmtFinType1'].unique())
calculateobspercentage(df_train, 'BsmtFinType1')
boxplotxy(df_train, 'BsmtFinType1', 'SalePrice')
# Decided to not to combine any variables

mapping = {"None": 1, "Rec": 2, "BLQ": 3, "LwQ": 4, "ALQ": 5, "Unf": 6, "GLQ": 7}
mapvariable(df_train, df_test, 'BsmtFinType1', mapping)

# HeatingQC
print(df_train['HeatingQC'].unique())
calculateobspercentage(df_train, 'HeatingQC')
boxplotxy(df_train, 'HeatingQC', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['Po', 'Fa']
replaceobserwations(df_train, df_test, 'HeatingQC', toreplace, 'Other')
print(df_train['HeatingQC'].unique())
boxplotxy(df_train, 'HeatingQC', 'SalePrice')

mapping = {"Other": 1, "TA": 2, "Gd": 3, "Ex": 4}
mapvariable(df_train, df_test, 'HeatingQC', mapping)

# KitchenQual
print(df_train['KitchenQual'].unique())
calculateobspercentage(df_train, 'KitchenQual')
boxplotxy(df_train, 'KitchenQual', 'SalePrice')
# Decided to not to combine any variables

mapping = {"Ex": 1, "Gd": 2, "TA": 3, "Fa": 4}
mapvariable(df_train, df_test, 'KitchenQual', mapping)

# FireplaceQu
print(df_train['FireplaceQu'].unique())
calculateobspercentage(df_train, 'FireplaceQu')
boxplotxy(df_train, 'FireplaceQu', 'SalePrice')
# Decided to not to combine any variables

mapping = {"Po": 1, "None": 2, "Fa": 3, "TA": 4, "Gd": 5, "Ex": 6}
mapvariable(df_train, df_test, 'FireplaceQu', mapping)

# GarageType
print(df_train['GarageType'].unique())
calculateobspercentage(df_train, 'GarageType')
boxplotxy(df_train, 'GarageType', 'SalePrice')
# Decided to create 'Other' observation for two three popular ones

toreplace = ['2Types', 'CarPort', 'Basment']
replaceobserwations(df_train, df_test, 'GarageType', toreplace, 'Other')
print(df_train['GarageType'].unique())
boxplotxy(df_train, 'GarageType', 'SalePrice')

mapping = {"None": 1, "Detchd": 2, "Other": 3, "Attchd": 4, "BuiltIn": 5}
mapvariable(df_train, df_test, 'GarageType', mapping)

# GarageFinish
print(df_train['GarageFinish'].unique())
calculateobspercentage(df_train, 'GarageFinish')
boxplotxy(df_train, 'GarageFinish', 'SalePrice')
# Decided to not to combine any variables

mapping = {"None": 1, "Unf": 2, "RFn": 3, "Fin": 4}
mapvariable(df_train, df_test, 'GarageFinish', mapping)

print(df_test.info())
print(df_train.info())


# Saving data
df_train.to_csv('Data/train_V4.csv', index=True)
df_test.to_csv('Data/test_V4.csv', index=True)

