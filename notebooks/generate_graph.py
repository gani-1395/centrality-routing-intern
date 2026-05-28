import matplotlib.pyplot as plt
import networkx as nx

# 1. Create a 20-node random graph (Erdos-Renyi model)
# 20 nodes, and a 30% (0.3) probability of an edge between any two nodes
G = nx.erdos_renyi_graph(20, 0.3, seed=42)

# 2. Print network properties to the console
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

# Count the number of connected components (isolated groups of nodes)
num_components = nx.number_connected_components(G)
print(f"Number of connected components: {num_components}")

# 3. Draw and save the graph visual
plt.figure(figsize=(8, 6))
nx.draw(
    G,
    with_labels=True,
    node_color="skyblue",
    node_size=500,
    edge_color="gray",
    font_weight="bold",
)
plt.title("First 20-Node Random Network Graph")

# Save the plot inside your results directory
plt.savefig("results/first_graph.png")
print("Graph saved successfully to results/first_graph.png!")

# Display the graph window
plt.show()