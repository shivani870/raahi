import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

data_nodes = pd.read_csv('~/nodedata.csv')

data_nodes.head()

x = data_nodes.drop(['Node_id', 'Class', 'Network_type'], axis=1).values
y = data_nodes['Class'].values

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

ml = LinearRegression()
ml.fit(x_train, y_train)

y_pred = ml.predict(x_test)
print(y_pred)

ml.predict([[4, 2.2, 6, 64, 62]])

plt.figure(figsize=(15,10))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')

plt.show(block=True)

pred_y_df = pd.DataFrame({'Actual Value':y_test, 'Predicted Value':y_pred, 'Difference':y_test-y_pred})
pred_y_df