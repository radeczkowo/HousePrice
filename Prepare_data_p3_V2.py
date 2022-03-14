from Functions import *


pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V3.csv", index_col=0)
df_test = pd.read_csv("Data/test_V3.csv", index_col=0)

print(df_train.info())
print(df_test.info())

# Creating nw variables

# TotalPorch = ScreenPorch + 3SsnPorch + EnclosedPorch + OpenPorchSF
# Exterior = Exterior1st * Exterior2nd
# FireQ = Fireplaces * FireplaceQu
# Kitchen = KitchenAbvGr * KitchenQual

# MS = MSSubClass * MSZoning
df_train['MS'] = df_train['MSSubClass'] * df_train['MSZoning']
df_test['MS'] = df_test['MSSubClass'] * df_test['MSZoning']

# Bath = FullBath  + HalfBath + BsmtFullBath + BsmtHalfBath

df_train['Bath'] = df_train['FullBath'] + df_train['BsmtFullBath'] + df_train['HalfBath'] + df_train['BsmtHalfBath']
df_test['Bath'] = df_test['FullBath'] + df_test['BsmtFullBath'] + df_test['HalfBath'] + df_test['BsmtHalfBath']

# Style = HouseStyle * RoofStyle

df_train['Style'] = df_train['HouseStyle'] * df_train['RoofStyle']
df_test['Style'] = df_test['HouseStyle'] * df_test['RoofStyle']

# Bsmt = Foundation * BsmtFinType1

df_train['Bsmt'] = df_train['Foundation'] * df_train['BsmtFinType1']
df_test['Bsmt'] = df_test['Foundation'] * df_test['BsmtFinType1']

# TotaAbvGrd = FullBath + TotRmsAbvGrd + BsmtFullBath

df_train['TotaAbvGrd'] = df_train['FullBath'] + df_train['TotRmsAbvGrd'] + df_train['BsmtFullBath']
df_test['TotaAbvGrd'] = df_test['FullBath'] + df_test['TotRmsAbvGrd'] + df_test['BsmtFullBath']

# TotalArea = TotalBsmtSF+ GrLivArea

df_train['TotalArea'] = df_train['GrLivArea'] + df_train['TotalBsmtSF'] + df_train['GarageArea']
df_test['TotalArea'] = df_test['GrLivArea'] + df_test['TotalBsmtSF'] + df_test['GarageArea']

# OverallQC = OverallQual * OverallCond

df_train['OverallQC'] = df_train['OverallQual'] * df_train['OverallCond']
df_test['OverallQC'] = df_test['OverallQual'] * df_test['OverallCond']

print(df_train.info())
print(df_train.corr())

# Saving data
df_train.to_csv('Data/train_V4.csv', index=True)
df_test.to_csv('Data/test_V4.csv', index=True)
