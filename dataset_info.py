import networkx as nx
import matplotlib.pyplot as plt
import queue
import random
import xlsxwriter
import collections

G = nx.Graph()

# G=nx.read_edgelist("dataset/Email-1133.edgelist")
# G=nx.read_edgelist("dataset/CA-Hep.edgelist")
# G=nx.read_edgelist("dataset/hamster.edgelist")
# G=nx.read_edgelist("dataset/PGP.edgelist")
# G=nx.read_edgelist("dataset/astro.edgelist")
G=nx.read_edgelist("dataset/facebook.edgelist")
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)  # degree sequence
# print(degree_sequence)
degreeCount = collections.Counter(degree_sequence)
# print(degreeCount)
s = 0
for deg, cnt in degreeCount.items():
    s = s + (deg ** 2) * (cnt / degree_sequence.__len__())

print("Nodes: " + str(G.number_of_nodes()))
print("Edges: " + str(G.number_of_edges()))
print(nx.is_connected(G))

average_degree = ((2 * G.number_of_edges()) / G.number_of_nodes())
print("<k>: " + str(average_degree))

r=nx.degree_assortativity_coefficient(G)
print("r: " + str(r))

C = nx.average_clustering(G)
print("C: " + str(C))

d = nx.average_shortest_path_length(G)
print("d: " + str(d))

l = []
for v in G:
    l.append(G.degree(v))

max_degree = max(l)
print("<kmax>: " + str(max(l)))
#
# # average_degree_2 = np.var(l)
average_degree_2 = s
print("<k²>: " + str(average_degree_2))
#
beta_c = (average_degree / (average_degree_2 - average_degree))
print("betaC: " + str(beta_c))
#
beta = 1.5 * beta_c
print("beta: " + str(beta))