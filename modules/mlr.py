import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Loading data
file_path = os.path.join('..', 'data', 'compiled_node_dataset.csv')
data_nodes = pd.read_csv(file_path)

data_nodes.head()

x = data_nodes.drop(['Node_id', 'Class', 'Network_type', 'Range'], axis=1).values
y = data_nodes['Class'].values

print(x)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

ml = LinearRegression()
ml.fit(x_train, y_train)

y_pred = ml.predict(x_test)
print(y_pred)

plt.figure(figsize=(15,10))
plt.scatter(y_test, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')

pred_y_df = pd.DataFrame({'Actual Value':y_test, 'Predicted Value':y_pred, 'Difference':y_test-y_pred})
pred_y_df