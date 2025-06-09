from collections import deque

def dfs_iteractive_path(graph, start_node, target_node):
    stack = [(start_node, [start_node])]

    visited_nodes = set()

    while stack:
        current_node, path_to_current = stack.pop()

        if current_node == target_node:
            return path_to_current
        
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)

            neighbors = list(graph.neighbors(current_node))
            neighbors_reversed = list(reversed(neighbors))

            for neighbor in neighbors_reversed:
                if neighbor not in visited_nodes:
                    new_path = path_to_current + [neighbor]
                    stack.append((neighbor, new_path))
    return None

def bfs_interative_path(graph, start_node, target_node):
    queue = deque([(start_node, [start_node])])
    visited_nodes=set()

    while queue:
        current_node, path_to_current = queue.popleft()

        if current_node == target_node:
            return path_to_current
        
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)

            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited_nodes:
                    queue.append((neighbor, path_to_current + [neighbor]))

    return None
