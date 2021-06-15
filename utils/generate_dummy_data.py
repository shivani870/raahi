import os
import random
import sys
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    file_name = os.path.join('..' ,'data', sys.argv[1] + '.csv') 
    number_of_records = int(sys.argv[2])

    file = open(file_name, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(["Node_id", "RAM", "CPU", "Battery", "Internal", "Class", "Range", "Network_type"])

    rng = random.SystemRandom()
    ram_memory_size = [1, 2, 3, 4, 6, 8]
    internal_memory_size = [4, 8, 16, 32, 64]
    i = 0
    while i < number_of_records:
        i = i + 1

        node_id = i
        ram = rng.choice(ram_memory_size)
        cpu = round(rng.uniform(1, 3.5), 1)
        
        battery = rng.randrange(5, 101)
        internal = rng.choice(internal_memory_size)
        network_class = 0

        if ((battery >= 80 and internal >= 60) or (battery >= 80 and (internal < 60 and internal > 20)) or ((battery < 80 and battery > 10) and internal >= 60) or ((battery < 80 and battery > 10) and (internal < 60 and internal > 20))):
            network_class = 1
        elif ((battery >= 80 and internal <= 20) or ((battery < 80 and battery > 10) and internal <= 20)):
            network_class = 2
        elif ((battery <= 10 and internal >= 60) or (battery <= 10 and (internal < 60 and internal > 20))):
            network_class = 3
        else:
            network_class = 4
            
        range = rng.randrange(1, 150)
        network_type = ''

        if (range <= 10):
            network_type = 'Bluetooth'
        elif (range > 10 and range <= 100):
            network_type = 'MANET'
        else:
            network_type = 'DTN'

        writer.writerow([node_id, ram, cpu, battery, internal, network_class, range, network_type])
except:
    print('Give me a file name and the number of nodes you want to generate')