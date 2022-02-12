# Graph
# ------------
# A graph is a data structure that is non-linear that consists of nodes and edges.
# Commonly nodes are called as vertices, and an each vertices hold other nodes.
# A graph is comonly used to represent a network (social network, circuits, paths, etc.)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Graph:
    def __init__(self, verticies):
        self.vertices = verticies
        self.graph = [None] * self.verticies
    
    def AddEdge(self, source, destination):
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = Node(source)
        node.next = self.graph[destination]
        self.graph[destination] = node
