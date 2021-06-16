import os
import pandas as pd
from sklearn import metrics
import joblib
import matplotlib.pyplot as plt
  
# Loading data
file_path = os.path.join('data', 'test_dataset.csv')
data_nodes = pd.read_csv(file_path)

x = data_nodes[['Battery', 'Internal']].values
y = data_nodes['Class'].values

model_path = os.path.join('models', 'knn_model.pkl')  
knn = joblib.load(model_path)  

# Predict on dataset which model has not seen before
y_pred = knn.predict(x)

print("\nAccuracy:",metrics.accuracy_score(y, y_pred))

plt.figure(figsize=(10,10))
plt.scatter(y, y_pred)
plt.plot(y, y_pred)
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')

pred_y_df = pd.DataFrame({'Actual Value':y, 'Predicted Value':y_pred, 'Difference':y-y_pred})
pred_y_df