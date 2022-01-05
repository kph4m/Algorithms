# Breadth First Search
# Traverse vertices level wise
# Time Complexity: O(V+E)
# Space Complexity: O(V)

# use deque from collections library
import collections

# BFS
def BFS(graph, root):

    # initialize visited and queue
    visited, queue = set(), collections.deque([root])

    # add root to visited list
    visited.add(root)

    # while there are elements in the queue
    while queue:

        # Pop first element in queue (root)
        vertex = queue.popleft()

        print(str(vertex))

        # Loop through all neighbors of popped node
        for neighbor in graph[vertex]:
            # If it isn't visited, add it to visited and add to queue
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# initalize graph
graph = { '0': set(['1','2','3']),
        '1': set(['0', '4', '5']),
        '2': set(['0','6','7']),
        '3': set(['0', '8', '9']),
        '4': set(['1']),
        '5': set(['1']),
        '6': set(['2']),
        '7': set(['2']),
        '8': set(['3']),
        '9': set(['3'])
}

BFS(graph,'0')

