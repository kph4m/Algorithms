# Bellman Ford Algorithm
# Finds shortest path from vertex to all other vertexes in a weighted graph
# Check each vertex and each edge in each iteration (Dijkstra only checks neighbor vertex)
# Account for negative weights, which could lead to negative cycles (reduces path length)

# Create graph class
class Graph:
    # Initialization
    def __init__(self,vertices):
        # Number of vertices
        self.V = vertices

        # Array to store the edges
        self.graph = []

    
    # Add edges method
    # Start - starting node
    # Dest - ending node
    # Weight - weight of edge
    def addEdges(self, start, dest, weight):
        self.graph.append([start,dest,weight])

    # Print path and weight
    def print_path(self,dist):
        for i in range(self.V):
            print("{0}\t\t{1}".format(i,dist[i]))

    # BFA
    def BFA(self,src):
        # Set all distances of vertices to infinity
        dist = [float("Inf")] * self.V

        # Set distance of source to 0
        dist[src] = 0

        # For all vertices except the first one
        for _ in range(self.V - 1):
            # For all start, dest, and weight in graphs
            for start,dest,weight in self.graph:
                # If distance of start not infinity and distance of start + weight is less than distance of destination
                if dist[start] != float("Inf") and dist[start] + weight < dist[dest]:
                    # set distance of destination to distance of start + w (lowest path)
                    dist[dest] = dist[start] + weight


        # Check for negative weight cycles by checking if lower path found
        # For all start, dest, and weight in graphs
        for start,dest,weight in self.graph:
            # If path length changed again
            if dist[start] != float("Inf") and dist[start] + weight < dist[dest]:
                print("Negative weight cycle detected")
                # Exit
                return
        
        # If no negative weight cycle, print path and weight
        self.print_path(dist)
                
# Initialize graph
g = Graph(5)
g.addEdges(0, 1, 5)
g.addEdges(0, 2, 4)
g.addEdges(1, 3, 3)
g.addEdges(2, 1, 6)
g.addEdges(3, 2, 2)
g.BFA(0)
            