from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np
df_income=pd.read_csv("/Users/amark/Desktop/Py4e/Puzzles/MEHOINUSIAA646N.csv")
df_income["Date"]=df_income["Date"]-1984
# print(df_population)
X1b = df_income['Date'].values
y1b = df_income.Income.values
X1bC = sm.add_constant(X1b)
X_train1b, X_test1b, y_train1b, y_test1b = train_test_split(X1bC, y1b, test_size=0.3, random_state=0)
training = sm.OLS(y_train1b, X_train1b).fit()
print(training.summary())
fig = plt.figure()  # an empty figure with no Axes
fig, ax = plt.subplots()  # a figure with a single Axes
y_hat1=training.predict(X_test1b)
X_train_plain=[y[1] for y in X_test1b]
plt.scatter(X_train_plain,y_test1b,c='r')
plt.scatter(X_train_plain,y_hat1,c='b')
plt.show()

