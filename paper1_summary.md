Literature Review: Centrality-Based Wireless Routing Survey

# 1. Core Problem Statement
Routing packets in wireless networks (MANETs/VANETs/IoT meshes) is highly complex due to:
* Dynamic Topologies: Continuous node mobility causes frequent link breaks and path recalculations.
* Resource Constraints: Nodes operate with limited battery power, processing capacity, and bandwidth.
* Traffic Inequities: Traditional shortest-path routing (e.g., AODV) ignores load, routing packets blindly through the same paths, which accelerates node failure via battery exhaustion and buffer congestion.

# 2. Centrality Metrics Used
Graph theory metrics identify structural "anchors" to improve routing decisions:
* Degree Centrality:Highlights locally well-connected nodes, optimal for data broadcasting or cluster-head selection.
* Betweenness Centrality: Identifies topological bridges controlling the flow of information; used to locate high-traffic relay hubs.
* Closeness Centrality: Measures the speed at which a node can distribute information to all other nodes, minimizing end-to-end latency.
* Eigenvector Centrality: Flags nodes connected to *other* major hubs, mapping out the structural backbone of the network.

# 3. Traditional Routing Logic
Existing protocols employ hand-crafted heuristics using these metrics:
* Greedy Forwarding: Packets are passed to the neighbor with the highest centrality score under the assumption that it possesses the best global reach.
* Cluster-Based Routing: Networks are segmented into communities where the node with the highest centrality is chosen as the message broker.
* Load Balancing (Thresholding): Logic diverts traffic to lower-centrality paths if a primary hub's packet queue exceeds a set safety threshold.

# 4. Open Gaps & Limitations
* High Control Overhead: Calculating global metrics like Betweenness Centrality requires constant network-wide flooding of topology packets, rapidly draining bandwidth and battery.
* Computation Latency: Centrality recalculation is slow. In mobile environments, paths change faster than the math can update, leading to stale routing decisions.
* Lack of Adaptability: Static heuristics cannot adapt to changing traffic patterns, predict bursts, or learn from historical packet drop failures.

This establishes the core objective of our project: Replacing rigid heuristics with Graph Neural Networks (GNNs) to learn fast, localized structural embeddings, combined with Deep Reinforcement Learning (DQN) to dynamically manage routing decisions in real time.
