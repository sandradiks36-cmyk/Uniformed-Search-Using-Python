
from bfs import bfs
from dfs import dfs
from iddfs import iddfs

import networkx as nx
import matplotlib.pyplot as plt

# Your graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
    }
#add your (code) graph here as a dictionary







# Create directed graph
G = nx.DiGraph()

# Add edges
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw
plt.figure(figsize=(6, 5))
pos = nx.circular_layout(G)  # auto layout

nx.draw(
    G, pos,
    with_labels=True,
    node_color='lightblue',
    node_size=2000,
    font_size=12,
    font_weight='bold',
    arrows=True
)

plt.title("Graph Representation")
plt.show()


start_node = 'A'   # change if your root is different

print("BFS:", bfs(graph, start_node))
print("DFS:", dfs(graph, start_node))
print("IDDFS:", iddfs(graph, start_node, 3))
