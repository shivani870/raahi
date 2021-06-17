import os
from chefboost import Chefboost as chef
import pandas as pd
import joblib

file_path = os.path.join('data', 'test_dataset.csv')
df = pd.read_csv(file_path)

features = df[['Battery', 'Internal']].values
decision = df['Class'].values

# merged_data = list(zip(battery, internal, node_class))

# formatted_df = pd.DataFrame(merged_data, columns = ['Battery', 'Internal', 'Decision'])

os.chdir('classification')
model = chef.load_model('regression_model.pkl')

prediction = chef.predict(model, all(features))

print(prediction)