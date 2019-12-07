# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 13:46:07 2019

@author: home
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#IMPORTING THE DATASET

dataset = pd.read_csv('aids.csv')
X = dataset.iloc[: , :-1].values
Y = dataset.iloc[: , 1].values

#SPLITTING THE DATASET INTO TRAIN AND TEST 
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 1/4, random_state = 0) #i set test_size = 1/4 b/c it gives best fit line may be

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predicting the Test set results
Y_pred = regressor.predict(X_test)

# Visualising the Training set results
plt.scatter(X_train, Y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Death vs Years (Training set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, Y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color = 'black')
plt.title('Death vs Years (Test set)')
plt.xlabel('Years')
plt.ylabel('Death')
plt.show()

print(regressor.predict([[2000]]))


