# Define the graph using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# Function to perform BFS
def bfs(graph, start_node):
    visited = []         # List to keep track of visited nodes
    queue = []           # Queue for BFS

    visited.append(start_node)
    queue.append(start_node)

    print("\nRESULT:")

    while queue:
        current = queue.pop(0)
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

# Main Code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()

# Check if the input node is valid
if snode in graph:
    bfs(graph, snode)
else:
    print("Invalid starting node.")
