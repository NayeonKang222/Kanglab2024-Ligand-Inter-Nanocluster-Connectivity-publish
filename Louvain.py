import network as nx
import community
G = nx.Graph()
G.add_edges_from([23])
partition = community.best_partition(G)
print("Node: Cluster") 
for node, cluster in partition.items(): 
     print(f"{node}: {cluster}")