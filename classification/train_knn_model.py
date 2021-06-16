import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

os.chdir(os.path.dirname(os.path.abspath(__file__)))
  
# Loading data
file_path = os.path.join('..', 'data', 'compiled_node_dataset.csv')
data_nodes = pd.read_csv(file_path)

x = data_nodes[['Battery', 'Internal']].values
y = data_nodes['Class'].values
  
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x, y)
  
# Save Model
save_model = os.path.join('..', 'models', 'knn_model.pkl')
joblib.dump(knn, save_model)