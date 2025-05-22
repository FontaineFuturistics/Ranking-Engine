import json
import random # To shuffle the nodes

class RankNode:
    def __init__(self, name: str):
        self.name = name
    def __repr__(self):
        return self.name

class RankGraph:
    """
    A class to represent a collection of items and to rank them.
    Each item is represented by a RankNode with directional edges
    An edge from node A to node B indicates that A is ranked lower than B.
    The graph is directed and can contain cycles.
    The graph is represented as an adjacency list.
    """

    # Constructor to load the graph from a json file
    def __init__(self, file_path: str):

        # Make the data structure
        self.adjacency_list = {}
        self.nodes = []

        # Read the json file and populate the graph
        with open(file_path, 'r') as file:
            data = json.load(file)

            # Add all nodes to graph
            for node_name in data.keys():
                node = RankNode(node_name)
                self.add_node(node)

            # Add all edges to graph
            for node in self.nodes:
                for neighbor in data[node.name]:
                    self.add_edge(node, neighbor)

    # Add a node to the graph
    def add_node(self, node: RankNode):
        if node.name not in self.adjacency_list:
            self.adjacency_list[node.name] = []
            self.nodes.append(node)

    # Add an edge to the graph
    def add_edge(self, from_node, to_node):
        # If from_node and to_node are strings, convert them to RankNode
        if isinstance(from_node, str):
            from_node = self.get_node(from_node)
        if isinstance(to_node, str):
            to_node = self.get_node(to_node)

        # Now that we have RankNode objects, we can add the edge
        if from_node and to_node:
            self.adjacency_list[from_node.name].append(to_node)
        else:
            raise ValueError(f"One or both nodes not found in the graph for {from_node} -> {to_node}")
        
    def print_graph(self):
        for node, edges in self.adjacency_list.items():
            for edge in edges:
                print(f"{node} -> {edge.name}")

    def get_node(self, name: str):
        for node in self.nodes:
            if node.name == name:
                return node
        return None
    
    def get_undirected_neighbors(self, node: RankNode):
        """
        Get all neighbors of a node in an undirected manner, i.e., both directions.
        """

        # Outbound neighbors (make a copy to avoid modifying the original list)
        neighbors = list(self.adjacency_list[node.name])
        # Then add all inbound neighbors
        for n in self.nodes:
            if node in self.adjacency_list[n.name]:
                neighbors.append(n)

        return neighbors
    
    def get_indirect_neighbors(self, node: RankNode):
        """
        Get all indirect neighbors of a node, includes self to avoid cycles getting an extra node.
        """
        
        # Make the list of indirect neighbors
        indirect_neighbors = []

        def dfs(current_node):
            indirect_neighbors.append(current_node)
            for neighbor in self.adjacency_list[current_node.name]:
                if neighbor not in indirect_neighbors:
                    dfs(neighbor)

        dfs(node)
        return indirect_neighbors

    # Get all connected components in the graph
    def get_connected_components(self):
        visited = set()
        components = []

        def dfs(node, component):
            visited.add(node.name)
            component.append(node)
            for neighbor in self.get_undirected_neighbors(node):
                if neighbor.name not in visited:
                    dfs(neighbor, component)

        for node in self.nodes:
            if node.name not in visited:
                component = []
                dfs(node, component)
                components.append(component)

        return components
    
    # Return whether we can make a list
    def can_make_list(self) -> bool:
        """
        Check if the graph can be made into a list.
        """
        return (len(self.get_connected_components()) == 1)
    
    # Make the list
    def make_list(self) -> list:
        """
        Order the nodes in the graph into a best-fit list considering the cycles
        """

        if not self.can_make_list():
            raise ValueError("Graph cannot be made into a list")
        
        # Get the list of indirect neighbors for all nodes
        indirect_neighbors = {}
        for node in self.nodes:
            indirect_neighbors[node.name] = self.get_indirect_neighbors(node)

        # Sort the nodes by the number of indirect neighbors
        sorted_nodes = sorted(self.nodes, key=lambda x: len(indirect_neighbors[x.name]), reverse=False)
     
        # Return the sorted list of nodes
        return sorted_nodes

    # Next nodes to compare
    def next_nodes(self) -> tuple:
        """
        Get the next nodes to compare in the graph,
        If there are multiple connected components, return the first node of the first two components
        If there is a single connected component, return the node with the least undirected neighbors 
            and a node it has not been compared with
        """    

        components = self.get_connected_components()
        if len(components) > 1:
            return components[0][0], components[1][0]
        else:
            # Get the node with the least undirected neighbors
            min_node = min(self.nodes, key=lambda x: len(self.get_undirected_neighbors(x)))
            # Get a node it has not been compared with
            shuffled_nodes = list(self.nodes)
            random.shuffle(shuffled_nodes)
            for node in shuffled_nodes:
                if node.name != min_node.name and node not in self.get_undirected_neighbors(min_node):
                    return min_node, node
            # If all nodes have been compared, return None
            return None, None
        
    def get_edge_count(self):
        """
        Get the number of edges in the graph.
        """
        count = 0
        for node in self.nodes:
            count += len(self.adjacency_list[node.name])
        return count

    def save(self, file_path: str):
        """
        Save the graph to a json file.
        """
        data = {}
        for node in self.nodes:
            data[node.name] = [neighbor.name for neighbor in self.adjacency_list[node.name]]
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == "__main__":
    
    import misc

    graph = RankGraph("./data/example_1CC.json")

    graph.next_nodes()