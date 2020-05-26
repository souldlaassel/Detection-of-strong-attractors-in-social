import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
                  ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
                  ("C", "J"), ("C", "K")])



# print(nx.adj_matrix(G))
A = nx.adjacency_matrix(G)
# print(type((A.todense()).shape))
# print(A.todense().item((1,1)))
# print('\n\n')
#
# print()

x = dict([(n,1.0/len(G)) for n in G])
print(x)
s = 1.0/sum(x.values())
print(len(G))
print(A.shape)
print(G.number_of_nodes())
print(G['A'])
for k in x:
    print(k)
# print(len(G))