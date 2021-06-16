import os
from chefboost import Chefboost as chef
import pandas as pd

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = os.path.join('..', 'data', 'compiled_node_dataset.csv')
df = pd.read_csv(file_path)

battery = df['Battery'].values
internal = df['Internal'].values
node_class = df['Class'].values

merged_data = list(zip(battery, internal, node_class))

formatted_df = pd.DataFrame(merged_data, columns = ['Battery', 'Internal', 'Decision'])

config = {'algorithm': 'Regression', 'enableRandomForest': True, 'num_of_trees': 5}
model = chef.fit(formatted_df, config)

chef.save_model(model, 'regression_model.pkl')