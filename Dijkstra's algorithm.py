#Initializing the Graph Class

from collections import defaultdict
class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
    
    def addNode(self,value):      #add node
        self.nodes.add(value)
    
    def addEdge(self, fromNode, toNode, distance):          #add edge
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = distance

# dikstra Algorithm
def dikstra(graph, initial):
    visited = {initial : 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None       #the first  amount is None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node      
                elif visited[node] < visited[minNode]:   #if we found a node which is fewer than minNode, we put that node in minNode
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]                 

        for edge in graph.edges[minNode]:                 
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)
    
    return visited, path              #it returns visited nodes and path(I draw on paper)


#example
#the difinition of code is in my document, I have explained before very clearly step by step, on paper
#I draw the nodes on paper
customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)

print(dikstra(customGraph, "A"))

