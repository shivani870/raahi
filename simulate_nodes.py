from modules import generate_coordinates


coordinates = generate_coordinates.generateRandomPoints({'lat': 34.2157, 'lng': 75.5041}, 1000, 2)

print(coordinates)


# import networkx as nx


# G = nx.Graph()
# G.add_nodes_from([2, 3])

# G.add_edges_from([(1, 2), (1, 3)])

# # G.number_of_edges()
# G.number_of_nodes()