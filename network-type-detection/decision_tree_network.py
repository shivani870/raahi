import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
import joblib

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Loading data
file_path = os.path.join('..', 'data', 'compiled_node_dataset.csv')
data_nodes = pd.read_csv(file_path)

x = data_nodes[['Class', 'Range']].values
y = data_nodes['Network_type'].values

dtc = DecisionTreeClassifier()

dtc = dtc.fit(x, y)

save_model = os.path.join('..', 'models', 'network_prediction_model.pkl')
joblib.dump(dtc, save_model)