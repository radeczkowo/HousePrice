from Functions import *


pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)



df_all = pd.read_csv("Data/all_V1.csv", index_col=0)

df_train = df_all.loc[df_all[['SalePrice']].notnull().any(axis=1)]
df_test = df_all.loc[df_all[['SalePrice']].isnull().any(axis=1)]
df_test = df_test.drop(columns=['SalePrice'])
print(df_train.info())
print(df_test.info())


for n in df_all.select_dtypes(include=np.number).columns:
    # boxplot = df_all.boxplot(column=n)
    # plt.show()
    plt.scatter(x=df_train[n], y=df_train['SalePrice'])
    plt.xlabel(n)
    plt.ylabel("SalePrice")
    #plt.show()

'''

for var in df_all.drop(columns='SalePrice').select_dtypes(include=np.number).columns:
    df_all[var] = replacingoutlieriqr(df_all[var])
'''


# Saving data
df_train.to_csv('Data/train_V2.csv', index=True)
df_test.to_csv('Data/test_V2.csv', index=True)

