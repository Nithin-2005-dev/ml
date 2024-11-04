# -*- coding: utf-8 -*-
"""linear_regression_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E6umnHTXxto3rrM5XJGLWXZd88oXOe2X

Linear Regression:

**Y=wX+b**

Y->Dependent Variable

X->Independent variable

w->weight

b->bias

**Gradient Descent:**

Gradient Descent is an optimization algorithm used for minimizing the loss function in variou machine learning algorithms.It is used for updating the parameters of the learning model.

w=w-a*dw

b=b-a*db

**Learning Rate:**

Learning rate is a tuning parameter in an optimization algorithm that determines the step size at each iteration while moving toward a minimum of a loss function

**dw=-2/n∑xi(yi-yipred)**


**db=-2/n∑(yi-yipred)**
"""

import numpy as np

class Linear_Regression():
    def __init__(self,learning_rate,no_of_iterations) :
      self.learning_rate=learning_rate
      self.no_of_iterations=no_of_iterations
    def fit(self,X,Y):
      self.m,self.n=X.shape
      self.w=np.zeros(self.n)
      self.b=0
      self.X=X
      self.Y=Y
      for i in range(self.no_of_iterations):
        self.update_weights()
    def update_weights(self,):
      Y_predection=self.predict(self.X)
      dw=-(2*(self.X.T.dot(self.Y-Y_predection)))/self.m
      db=-2*np.sum(self.Y-Y_predection)/self.m
      self.w=self.w-self.learning_rate*dw
      self.b=self.b-self.learning_rate*db
    def predict(self,X):
      return X.dot(self.w)+self.b

import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

dataset=pd.read_csv('models\salary_data.csv')

dataset.head()

plt.scatter(dataset['YearsExperience'],dataset['Salary'],color='r')
x=np.linspace(1,10,100000)
# print(x)
plt.plot(x,x*9158.236339779503+26136.59700431744)

dataset.shape

dataset.isnull().sum()

data=dataset.iloc[:,:-1].values
target=dataset.iloc[:,1].values

print(data,target)

data_train,data_test,target_train,target_test=train_test_split(data,target,test_size=0.33,random_state=1)

model=Linear_Regression(learning_rate=0.02,no_of_iterations=1000)

model.fit(data_train,target_train)

print(model.w[0],model.b)

test_data_prediction=model.predict(data_test)
print(test_data_prediction)

