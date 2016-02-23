import pandas as pd
import statsmodels.api as sm
from sklearn import preprocessing

df = pd.read_csv('loansData.csv')

min_max_scaler = preprocessing.MinMaxScaler()


df.loc[(df['Monthly.Income'].isnull()), 'Monthly.Income'] = 0
Y = df['Loan.Amount']
# Y = min_max_scaler.fit_transform(Y.values)

# ['Interest.Rate', 'FICO.Score', 'Loan.Length', 'Monthly.Income']
X = df.drop(['Loan.Amount'], axis=1)
# X = min_max_scaler.fit_transform(X)
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print results.params
print results.tvalues

X = df['Interest.Rate']
# X = min_max_scaler.fit_transform(X)
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print results.params
print results.tvalues

X = df['Loan.Length']
# X = min_max_scaler.fit_transform(X)
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print results.params
print results.tvalues

X = df['FICO.Score']
# X = min_max_scaler.fit_transform(X)
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print results.params
print results.tvalues

X = df['Monthly.Income']
# X = min_max_scaler.fit_transform(X)
X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print results.params
print results.tvalues