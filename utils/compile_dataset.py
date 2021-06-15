import os
import sys
import csv
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

number_of_arguments = len(sys.argv)
out_file_path = os.path.join('..', 'data', 'compiled_node_dataset.csv')

out_file = open(out_file_path, 'w', newline='')
writer = csv.writer(out_file)
writer.writerow(["Node_id", "RAM", "CPU", "Battery", "Internal", "Class", "Range", "Network_type"])

node_id = 1
for i in range(1, number_of_arguments):
    file_path = os.path.join('..', 'data', sys.argv[i])
    print("Reading data from ", file_path)

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if (row[4] == '3' or row[4] == '4'):
                writer.writerow([node_id, row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
                node_id = node_id + 1    
            else:
                if(0.5 < random.random()):
                    writer.writerow([node_id, row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
                    node_id = node_id + 1