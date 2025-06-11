import heapq
from task_1 import G, start, finish

weighted_roads =[
    ('A', 'B', 4), ('A', 'C',2), ('B', 'D',5), ('C','D', 1), ('D', 'E',3), ('E', 'F',1), ('C', 'F',7)
]

for u, v, weight in weighted_roads:
    if G.has_edge(u, v):
        G[u][v]['weight'] = weight
    else:
        G.add_edge(u,v, weight=weight)


def dijkstra(graph, start_node, target_node):
    queue=[(0, start_node, [start_node])]
    visited = set()
    distances = {start_node: 0}

    while queue:
        current_cost, current_node, path = heapq.heappop(queue)

        if current_node == target_node:
            return path, current_cost
        
        if current_node in visited:
            continue

        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            edge_weight = graph[current_node][neighbor]['weight']
            total_cost = current_cost + edge_weight
            if neighbor not in distances or total_cost < distances[neighbor]:
                
                distances[neighbor] = total_cost
                heapq.heappush(queue, (total_cost, neighbor, path + [neighbor]))

    return None

path, cost = dijkstra(G, start, finish)
print(f"Найкоротший шлях від {start} до {finish}: {path}, вага {cost}")