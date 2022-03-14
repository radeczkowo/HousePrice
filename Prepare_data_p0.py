from Functions import *

# Output variable analysis

df_train = pd.read_csv("Data/train_V1.csv", index_col=0)
df_test = pd.read_csv("Data/test_V1.csv", index_col=0)

print(df_train.info())

print(df_train['SalePrice'].skew())
print(df_train['SalePrice'].kurt())
df_train['SalePrice'].plot.kde(bw_method=1)
plt.show()
print(df_train.info())


df_all = pd.concat([df_train, df_test])

df_all.to_csv('Data/all_V0.csv', index=True)
