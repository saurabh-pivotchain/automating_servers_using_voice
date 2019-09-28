#!/usr/bin/python36
import subprocess as sp
import pandas as pd
import cgi
print("content-type: text/html")
print()
form = cgi.FieldStorage()
#a = form.getvalue("data")
#value = form.getvalue("pred")
dataset = pd.read_csv("Salary_Data.csv")
x = dataset.iloc[: , 0:1]
y = dataset.iloc[: , -1]
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x , y)
y_pred = model.predict([[3]])
print("Predicted value is: {}".format(y_pred))
