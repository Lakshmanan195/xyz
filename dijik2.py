import heapq

def dijkstra(graph, source):
    # Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}  # All distances set to infinity
    distances[source] = 0  # Distance to the source is 0
    priority_queue = [(0, source)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip processing if we've already found a shorter path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph as an adjacency list
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('C', 1), ('D', 7)],
    'C': [('D', 3)],
    'D': []
}

# Execute Dijkstra's algorithm
source = 'A'
shortest_distances = dijkstra(graph, source)

# Output the shortest distances from the source
print(f"Shortest distances from {source}:")
for node, distance in shortest_distances.items():
    print(f"{node}: {distance}")
