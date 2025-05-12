import networkx as nx
G = nx.path_graph(20)
centrality = nx.eigenvector_centrality_numpy(G)
for n in centrality:
  print ("c(", n, ")=", centrality[n])
