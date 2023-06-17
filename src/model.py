import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

import pickle

df = pd.read_csv('diamonds.csv')
X = df[['carat','depth','table','x','y','z']]
y = df['price']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state= 123)

# Scaling the features
sc = StandardScaler()
sc.fit_transform(X_train)
sc.transform(X_test)

# Applying model

lr = LinearRegression()
lr.fit(X_train,y_train)


# Saving the model

pickle.dump(lr,open('linear_regressor.pkl','wb'))

# Loading the model
model = pickle.load(open('linear_regressor.pkl','rb'))

# Testing the model
print(model.predict([[0.79,61.74,57.45,5.73,5.73,3.53]]))