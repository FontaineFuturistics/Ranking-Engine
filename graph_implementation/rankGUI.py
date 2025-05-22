import rank_graph
import misc
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog, scrolledtext

class RankUI:
    def __init__(self, graph: "rank_graph.RankGraph"):
        self.graph = graph
        self.root = tk.Tk()
        self.root.title("Ranking Engine")
        self.create_widgets()
        self.update_edge_count()
        self.next_nodes = None

    def create_widgets(self):
        # Frame for compare section
        self.compare_frame = tk.LabelFrame(self.root, text="Compare Next Nodes")
        self.compare_frame.pack(fill="x", padx=10, pady=5)

        self.compare_label = tk.Label(self.compare_frame, text="Click 'Compare Next' to begin.")
        self.compare_label.pack(side="left", padx=5)

        self.yes_button = tk.Button(self.compare_frame, text="Yes", state="disabled", command=lambda: self.handle_compare('y'))
        self.yes_button.pack(side="left", padx=2)
        self.no_button = tk.Button(self.compare_frame, text="No", state="disabled", command=lambda: self.handle_compare('n'))
        self.no_button.pack(side="left", padx=2)
        self.next_button = tk.Button(self.compare_frame, text="Compare Next", command=self.prepare_compare)
        self.next_button.pack(side="left", padx=5)

        # Frame for actions
        self.action_frame = tk.Frame(self.root)
        self.action_frame.pack(fill="x", padx=10, pady=5)

        self.print_list_button = tk.Button(self.action_frame, text="Print Current List", command=self.print_list)
        self.print_list_button.pack(side="left", padx=5)

        self.print_raw_button = tk.Button(self.action_frame, text="Print Raw Graph Data", command=self.print_raw_data)
        self.print_raw_button.pack(side="left", padx=5)

        self.save_button = tk.Button(self.action_frame, text="Save Graph Data", command=self.save_graph)
        self.save_button.pack(side="left", padx=5)

        self.exit_button = tk.Button(self.action_frame, text="Exit", command=self.root.quit)
        self.exit_button.pack(side="left", padx=5)

        # Frame for output
        self.output_frame = tk.LabelFrame(self.root, text="Output")
        self.output_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, height=15, width=70, state="disabled")
        self.output_text.pack(fill="both", expand=True)

        # Edge count label
        self.edge_count_label = tk.Label(self.root, text="Number of edges in the graph: 0")
        self.edge_count_label.pack(pady=5)

    def update_edge_count(self):
        count = self.graph.get_edge_count() if hasattr(self.graph, "get_edge_count") else len(getattr(self.graph, "edges", []))
        self.edge_count_label.config(text=f"Number of edges in the graph: {count}")

    def prepare_compare(self):
        try:
            node1, node2 = self.graph.next_nodes()
            self.next_nodes = (node1, node2)
            self.compare_label.config(text=f"Is '{node1.name}' ranked higher than '{node2.name}'?")
            self.yes_button.config(state="normal")
            self.no_button.config(state="normal")
        except Exception as e:
            self.compare_label.config(text="No more comparisons needed or error occurred.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
            messagebox.showinfo("Info", "No more comparisons needed or error occurred.")

    def handle_compare(self, choice):
        node1, node2 = self.next_nodes
        if choice == 'y':
            self.graph.add_edge(node2, node1)
        elif choice == 'n':
            self.graph.add_edge(node1, node2)
        self.compare_label.config(text="Click 'Compare Next' to continue.")
        self.yes_button.config(state="disabled")
        self.no_button.config(state="disabled")
        self.update_edge_count()

    def print_list(self):
        try:
            node_list = self.graph.make_list()
            output = "Ordered List:\n" + "\n".join(node.name for node in node_list)
            self.display_output(output)
        except Exception as e:
            self.display_output(f"Error printing list: {e}")

    def print_raw_data(self):
        try:
            output = "Raw graph data:\nNodes:\n"
            # Format nodes as a list of names for consistency
            output += "\n".join(node.name for node in self.graph.nodes)
            output += "\nAdjacency List:\n"
            # Format adjacency list as node: [neighbor1, neighbor2, ...]
            for node in self.graph.nodes:
                neighbors = self.graph.adjacency_list.get(node.name, [])
                neighbor_names = [n.name for n in neighbors]
                output += f"{node.name}: {neighbor_names}\n"
            self.display_output(output)
        except Exception:
            # fallback to print_list and print_dict if available
            import io
            import sys
            buf = io.StringIO()
            sys_stdout = sys.stdout
            sys.stdout = buf
            try:
                misc.print_list(self.graph.nodes)
                misc.print_dict(self.graph.adjacency_list)
            finally:
                sys.stdout = sys_stdout
            self.display_output(buf.getvalue())

    def save_graph(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filepath:
            try:
                self.graph.save(filepath)
                messagebox.showinfo("Success", f"Graph data saved to {filepath}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save graph: {e}")

    def display_output(self, text):
        self.output_text.config(state="normal")
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, text)
        self.output_text.config(state="disabled")

def main():
    graph = rank_graph.RankGraph("/Users/liame/Documents/GitHub/Ranking-Engine/graph_implementation/data/realdata.json")
    #graph = rank_graph.RankGraph("./data/example_2CC.json")
    app = RankUI(graph)
    app.root.mainloop()

if __name__ == "__main__":
    main()