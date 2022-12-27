import neuralfit as nf
import matplotlib.pyplot as plt
import networkx as nx
from itertools import count

# Create a random model
model = nf.Model(1,1,size=5)

# Get model neurons and connections
nodes = model.get_nodes()
connections = model.get_connections()

# Create a graph from nodes and connections
graph = nx.DiGraph()
graph.add_nodes_from(nodes)
graph.add_edges_from(connections)

# Give each activation function a unique color
groups = set(nx.get_node_attributes(graph,'activation').values())
mapping = dict(zip(sorted(groups),count()))
colors = [mapping[graph.nodes[n]['activation']] for n in graph.nodes()]

# Visualize the graph
nx.draw(graph, node_color=colors, with_labels=True)
plt.show()
