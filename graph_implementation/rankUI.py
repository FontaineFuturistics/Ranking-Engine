import rank_graph
import misc

class rankUI:

    # Constructor
    def __init__(self, graph: "rank_graph.RankGraph"):
        self.graph = graph
        self.make_valid()

    def make_valid(self) -> None:
        """
        Make the graph valid by repeatedly comparing the nodes
        returned by nextNodes() until the graph is valid.
        """

        # Compare the nodes
        while not self.graph.can_make_list():
            self.compareNext()

    def compareNext(self) -> None:
        """
        Compare the next two nodes in the graph.
        """
        # Get the nodes to compare
        node1, node2 = self.graph.next_nodes()

        # Compare the nodes
        print(f"Comparing {node1.name} and {node2.name}")
        while True:
            # Get the user's input
            choice = input(f"Is {node1.name} ranked higher than {node2.name}? (y/n): ")

            if choice.lower() == 'y':
                self.graph.add_edge(node2, node1)
                break
            elif choice.lower() == 'n':
                self.graph.add_edge(node1, node2)
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def print_list(self) -> None:
        """
        Print the ordered list of nodes.
        """
        node_list = self.graph.make_list()

        for node in node_list:
            print(node.name)

    def main(self) -> None:
        """
        Main function to run the UI.
        Allows the user to compare nodes, print the list, or exit.
        Shows the number of comparisons after each action.
        """
        while True:
            print("\nOptions:")
            print("1. Compare next nodes")
            print("2. Print current list")
            print("3. Print raw graph data")
            print("4. Save graph data")
            print("5. Exit")
            choice = input("Select an option (1/2/3/4/5): ")

            if choice == '1':
                self.compareNext()
            elif choice == '2':
                self.print_list()
            elif choice == '3':
                print("Raw graph data:")
                print("Nodes:")
                misc.print_list(self.graph.nodes)
                print("Adjacency List:")
                misc.print_dict(self.graph.adjacency_list)
            elif choice == '4':
                filepath = input("Enter the file path to save the graph data: ")
                self.graph.save(filepath)
                print(f"Graph data saved to {filepath}")
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, 4, or 5.")

            # Show the number of edges in the graph
            print(f"Number of edges in the graph: {self.graph.get_edge_count()}")
        
if __name__ == "__main__":
    # Create a graph object
    graph = rank_graph.RankGraph("./data/example_2CC.json")

    # Create a UI object
    ui = rankUI(graph)

    # Run the UI
    ui.main()