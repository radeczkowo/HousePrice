from Functions import *

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)


df_train = pd.read_csv("Data/train.csv", index_col=0)
df_test = pd.read_csv("Data/test.csv", index_col=0)

# Data Understanding

print(df_train.info())
# print(len(df_train.select_dtypes('object').columns))

'''
80 columns
43 columns of categorical data
37 columns of numerical data
'''

# Drop columns in which percentage of missing values  is greater than threshold given.
df_train, df_test = dropcolumnstesttrain(df_train, df_test, getcolumnswithdatamissing(df_train, 0.7))

# Categorical Variables pre-cleaning

# print(df_train.select_dtypes('object').info())

# Finding columns in which percentage of the share of one variable is greater than threshold given.
columns = []
for variable in df_train.select_dtypes('object').columns:
    if not observationpercentagetodrop(df_train.select_dtypes('object'), variable, 0.75):
        columns.append(variable)

print(columns)

# Dropping columns found before
df_train, df_test = dropcolumnstesttrain(df_train, df_test, columns)

# Saving pre-cleaned data
df_train.to_csv('Data/train_V1.csv', index=False)
df_test.to_csv('Data/test_V1.csv', index=False)









