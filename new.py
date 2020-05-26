# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.Graph()
# G.add_node('1')
# G.add_node('2')
# G.add_node('3')
# G.add_node('4')
# G.add_node('5')
# G.add_edge('1', '2')
# G.add_edge('2', '3')
# G.add_edge('3', '4')
# G.add_edge('4', '1')
# G.add_edge('4', '5')
# nx.draw_spectral(G)
# plt.show()
import networkx as nx
import matplotlib.pyplot as plt
import operator
from fractions import Fraction
G = nx.Graph()
# G.add_node(1)
# G.add_nodes_from([2,3])
# H = nx.path_graph(10)
# G.add_nodes_from(H)
# G.add_edge(1,2)
# e = (2,3)
# G.add_edge(*e)
# G.add_edges_from(H.edges())
# G.clear()

# G.add_edge(1, 2)
# H = nx.DiGraph(G)   # create a DiGraph using the connections from G
# print(list(H.edges()))
#
# edgelist = [(0, 1), (1, 2), (2, 3)]
# H = nx.Graph(edgelist)

# G.add_node(1)
# G.add_edge(1,2)
# G.add_edges_from([(1,2), (1,3)])
# G.add_node("spam")
# G.add_nodes_from("spam")
# G.add_edge(3,2)
# G[3][2]['color'] = "blue"
# G.remove_node(2)
# G.remove_nodes_from("spam")
# G.remove_edge(1,3)
# print(G.number_of_nodes())
# print(G.number_of_edges())
# print(list(G.nodes()))
# print(list(G.edges()))
# print(list(G.adj[1]))
# print(G.degree([2,3]))

# FG = nx.Graph()
# FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
# # print(type(a), type(b))
# for n, nbrs in FG.adj.items():
#    print(n)
#    print(nbrs)
#    for nbr, eattr in nbrs.items():
#        wt = eattr['weight']
#        if wt < 0.5: print('(%d, %d, %.3f)' % (n, nbr, wt))

# G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
#                   ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
#                   ("C", "J"), ("C", "K")])

G.add_edges_from([("A", "B"), ("A", "E"), ("A", "C"),
                  ("B", "C"), ("B", "E"), ("B", "G"), ("B", "H"),
                  ("C", "D"), ("C", "E"),
                  ("D", "E"), ("D", "F"), ("D", "G"),
                  ("E", "G"),
                  # ("F", "G"),
                  ("G", "H"), ("H", "I"), ("I", "J")])

print(nx.closeness_centrality(G))

# N = G.number_of_nodes()
# M = G.number_of_edges()
# print(N)
# print(M)

# G=nx.karate_club_graph()
# G=nx.davis_southern_women_graph()
# G=nx.dodecahedral_graph()
# G = nx.read_gml('football.gml')
# print("Node Degree")
# for v in G:
#     print('%s %s' % (v,G.degree(v)))


# degC = nx.degree_centrality(G)
# cloC = nx.closeness_centrality(G)
#
# print(max(degC.items(), key=operator.itemgetter(1))[0])
# print(max(cloC.items(), key=operator.itemgetter(1))[0])
# for i in degC:
#     print(i, format(degC[i], '.5f'), degC[i]*(N - 1),N - 1)
#
# print("#############################################")
#
# for i in cloC:
#     print(i, cloC[i])
# print(degC)

# centrality = nx.eigenvector_centrality(G)
# print(['%s %0.2f'%(node,centrality[node]) for node in centrality])



nx.draw(G,with_labels=True)
# nx.draw_networkx(FG)

plt.show()