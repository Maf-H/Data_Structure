# Date and time June 14 2024 04:03 pm
# @author : Mesfin Haftu
"""
Breadth first search is a search algorithm used in graphs, that searches through the nodes of a tree and finds the shortest path to the destination.
Big(O) time complexity: O(V + E) Vertex is node, Edge is connection
"""
from collections import deque

graph = {}
graph["Mes"] = ["Fitih", "Menilik", "Hager"]
graph["Fitih"] = ["Namrud", "Ethiop"]
graph["Menilik"] = ["Siem", "Yafet"]
graph["Hager"] = ["Msrak"]
graph["Namrud"] = ["Msrak"]
graph["Ethiop"] = []
graph["Siem"] = []
graph["Yafet"] = []
graph["Msrak"] = []

visited = [] # used to store visited vertices in the graph.


def bfs(starting):
    """ Let's use this bfs function to count number of vertices in the graph"""
    visited.append(starting)
    queue = deque()
    queue += graph[starting]
    
    
    while queue:
        node_name = queue.popleft() # removes the first node from the queue
        if not is_visited(node_name):
            queue += graph[node_name] # adds the node at the end of the queue
            visited.append(node_name) 
    return visited, len(visited)
            
def is_visited(name): 
    """This function checks if the vertex is visited or not"""
    if name in visited:
        return True
    return False

print(bfs("Mes"))
    