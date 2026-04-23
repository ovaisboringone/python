graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8},
    'D': {'B': 5, 'C': 8}
}

start = input("Enter start node: ")

dist = {}
visited = {}

for node in graph:
    dist[node] = float('inf')
    visited[node] = False

dist[start] = 0

for _ in graph:

    min_node = None
    min_distance = float('inf')

    for node in graph:
        if not visited[node] and dist[node] < min_distance:
            min_distance = dist[node]
            min_node = node

    visited[min_node] = True

    for neighbor in graph[min_node]:
        new_distance = dist[min_node] + graph[min_node][neighbor]

        if new_distance < dist[neighbor]:
            dist[neighbor] = new_distance

print("Shortest distances:", dist)
