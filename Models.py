from Functions import *
from sklearn.linear_model import LinearRegression
from sklearn import svm
from sklearn import linear_model
from sklearn.linear_model import TweedieRegressor
from sklearn.neighbors import NeighborhoodComponentsAnalysis, KNeighborsClassifier

pd.set_option('display.max_columns', 80)
pd.set_option('display.max_rows', 100)

df_train = pd.read_csv("Data/train_V5.csv", index_col=0)
df_test = pd.read_csv("Data/test_V5.csv", index_col=0)

submission_df = pd.read_csv("Data/sample_submission.csv", index_col=0).drop(columns=['SalePrice'])


print(df_test.info())
print(df_train.info())
df_train.reset_index(drop=True, inplace=True)
df_test.reset_index(drop=True, inplace=True)
print(df_train.head())
print(df_train.corr())

# Models


model = LinearRegression()
testmodel(df_train, model, 'SalePrice', 0.08)

model = svm.SVR(kernel='linear')
testmodel(df_train, model, 'SalePrice', 0.08)

model = linear_model.Ridge(alpha=5)
testmodel(df_train, model, 'SalePrice', 0.08)

model = linear_model.BayesianRidge()
testmodel(df_train, model, 'SalePrice', 0.08)

model = TweedieRegressor(power=1, alpha=5, link='log')
testmodel(df_train, model, 'SalePrice', 0.08)


'''
alphas = [0.01, 0.1, 0.5, 1, 2.5, 5, 10, 25, 50, 75, 100]
for n in alphas:
    model = linear_model.Ridge(alpha=n)
    testmodel(df_train, model, 'SalePrice', 0.08)
'''

# Final model
model = linear_model.Ridge(alpha=5)
finalprediction(model, df_train, df_test, 'SalePrice', submission_df)



