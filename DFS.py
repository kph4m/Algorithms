# Depth First Search
# Traverse vertices depth wise
# Time Complexity: O(V+E)
# Space Complexity: O(V)

# DFS
def dfs(graph, start, visited=None):
    # If there are no visited, add start to visited
    if visited is None:
        visited=set()
    visited.add(start)

    print(start)
    print(visited)

    # Recursively traverse through each node that hasn't been visited yet
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    
    # Return all visited nodes
    return visited


# Initialize graph
graph = { '0': set(['1','2','3']),
        '1': set(['0', '2']),
        '2': set(['0','1','4']),
        '3': set(['0']),
        '4': set(['2'])
}

dfs(graph, '0')