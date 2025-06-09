import networkx as nx
import matplotlib.pyplot as plt
from task_2 import dfs_iteractive_path, bfs_interative_path


G = nx.Graph()

intersections= ['A', 'B', 'C', 'D', 'E', 'F']

G.add_nodes_from(intersections)

roads = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C','D'), ('D', 'E'), ('E', 'F'), ('C', 'F')]
G.add_edges_from(roads)

plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='orange', edge_color='gray', node_size=1200, font_size=16)
plt.title("Модель транспортної мережі")
plt.show()

# Task 2

start ='A'
finish='F'

dfs_path = dfs_iteractive_path(G, start, finish)
bfs_path = bfs_interative_path(G, start, finish)
print("dfs path: ",dfs_path)
print("bfs path: ",bfs_path)

      

 
 
