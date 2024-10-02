import network as nx
import community
G = nx.Graph()
G.add_edges_from([(1,2), (1,3), (2,3)])
partition = community.best_partition(G)
print("Node: Cluster") 
for node, cluster in partition.items(): 
     print(f"{node}: {cluster}")