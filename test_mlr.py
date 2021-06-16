import os
import pandas as pd
from sklearn.metrics import r2_score
import joblib
import matplotlib.pyplot as plt


# Loading data
file_path = os.path.join('data', 'test_dataset.csv')
data_nodes = pd.read_csv(file_path)

x = data_nodes[['Battery', 'Internal']].values
y = data_nodes['Class'].values

model_path = os.path.join('models', 'mlr_model.pkl')
ml = joblib.load(model_path)

y_pred = ml.predict(x)

print("\nAccuracy:",r2_score(y, y_pred))

plt.figure(figsize=(15,10))
plt.scatter(y, y_pred, color='red')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Actual vs Predicted')

pred_y_df = pd.DataFrame({'Actual Value':y, 'Predicted Value':y_pred, 'Difference':y-y_pred})
pred_y_df