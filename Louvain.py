import networkx as nx
import community.community_louvain as community
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (1, 7), (2, 7), (2, 8),(3, 8), (3, 9), (4, 9), (4, 10), (5, 10), (5, 11), (6, 11), (8, 9), (9, 10), (7, 12), (7, 13), (8, 14), (9, 14), (9, 15), (10, 15), (11, 16), (11, 17), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (12, 18), (13, 18), (13, 19), (14, 19), (14, 20), (15, 20), (15, 21), (16, 21), (16, 22), (17, 22), (18, 19), (19, 20), (20, 21), (21, 22), (18, 23), (18, 24), (19, 24), (19, 25), (21, 26), (21, 27), (22, 27), (22, 28), (23, 24), (24, 25), (25, 26), (26, 27), (27, 28)])
partition = community.best_partition(G)
print("Node: Cluster")
for node, cluster in partition.items():
    print(f"{node}: {cluster}")
