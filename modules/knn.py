import pandas as pd
import os
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
  
# Loading data
file_path = os.path.join('..', 'data', 'node_dataset.csv')
data_nodes = pd.read_csv(file_path)

data_nodes.head()

x = data_nodes.drop(['Node_id', 'Class', 'Network_type', 'Range'], axis=1).values
y = data_nodes['Class'].values

print(x)
print(y)

# Split into training and test set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
  
knn = KNeighborsClassifier(n_neighbors=8)
  
knn.fit(x_train, y_train)
  
# Predict on dataset which model has not seen before
print(knn.predict(x_test))
knn.predict([[8, 2.8, 63, 256]])