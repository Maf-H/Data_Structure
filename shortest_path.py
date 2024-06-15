# Date and time Jun 14, 2024 07:36 pm
# @author : Mesfin Haftu
"""
This program uses Dijkstra's algorithm to find the shortest path between start and finish nodes in a graph.
"""
def shortest_path():
    """
    Dijkstra's algorithm to find the shortest path between start and finish nodes in a graph.
    :param start: start node
    :param finish: finish node
    :return: shortest path cost
    time complexity: O(E + v*log(v))
    """
    # initialize the graph
    graph = {"start":{"A": 6, "B": 2}, "A": {"finish": 1}, "B":{"A": 3, "finish": 5}, "finish": {}}
    
    # initialize the costs from 'start' to neighbors  
    costs = {}
    costs["A"] = graph["start"]["A"]
    costs["B"] = graph["start"]["B"]
    costs["finish"] = float("inf")
    
    # initialize the parent of current node
    parent = {}
    parent["A"] = "start"
    parent["B"] = "start"
    parent["finish"] = None
    
    # Store the visited nodes
    visited = []
    
    def find_lowest_cost_node(costs):
        """
        find the lowest cost node based on the costs
        :param costs: costs from 'start' to neighbors
        :return: lowest cost node
        time complexity: O(v)
       """
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node, cost in costs.items():
            if cost < lowest_cost and node not in visited:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    
    node = find_lowest_cost_node(costs)
    while node :
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys(): 
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:          
            # checks if previous node's cost is greater than new cost
                costs[n] = new_cost
                parent[n] = node # builds who is whose parent used for visualization purpose
        visited.append(node) # add the node to the visited list
        node = find_lowest_cost_node(costs) # find lowest cost node based on updated costs
    print(parent)
    print("From 'start'-> ", costs)    
    return costs

shortest_path()