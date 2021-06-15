import os
import sys
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))

number_of_arguments = len(sys.argv)
out_file_path = os.path.join('..', 'data', 'node_dataset.csv')

out_file = open(out_file_path, 'w', newline='')
writer = csv.writer(out_file)
writer.writerow(["Node_id", "RAM", "CPU", "Battery", "Internal", "Class", "Range", "Network_type"])

node_id = 1
for i in range(1, number_of_arguments):
    file_path = os.path.join('..', 'data', sys.argv[i])
    print("Reading data from ", file_path)

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if (row[5] == '3'):
                writer.writerow([node_id, row[1], row[2], row[3], row[4], row[5], row[6], row[7]])
                node_id = node_id + 1               