import networkx as nx
import matplotlib.pyplot as plt

# ================ Initialisation des Graph =================
G = nx.karate_club_graph()
######################################
# G=nx.davis_southern_women_graph()
######################################
# G=nx.dodecahedral_graph()
######################################
# G = nx.Graph()
# G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
#                   ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
#                   ("C", "J"), ("C", "K")])
######################################
# G = nx.read_gml('lesmiserables.gml')
edges = nx.read_edgelist('dataset/facebook.txt')
G.add_edges_from(edges.edges())

# ===========================================================

########## Degree Centrality #########
deg = {}
N = G.number_of_nodes()
for v in G:
    deg[v] = ((G.degree(v) / (N - 1)))

# print(deg)
maxDeg = max(deg.values())
# print(maxDeg)
######################################

##======== Affichage du réseau =======================
# dictR = close
# maxDictR = maxClose
dictR = deg
maxDictR = maxDeg
###### LAbels ####################
labels = {}# print(labels)

i = 0
for key, value in dictR.items():
    labels[i] = str(key) + "\n" + str(float("{0:.2f}".format(value)))
    i = i + 1
######################################

########## Positions To int ##########
pos = nx.spring_layout(G)
posI = {}
i = 0
for key, value in pos.items():
    posI[i] = value
    i = i + 1
# print(pos)
# print(posI)
######################################
nx.draw_networkx_nodes(G, pos,
                       node_color='b',
                       node_size=[(i / maxDictR) * 200 for i in list(dictR.values())],
                       alpha=1)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.8)
# nx.draw_networkx_labels(G, posI, labels, font_size=8)
# nx.draw_networkx(G)
plt.axis('off')
plt.show()
# ===================================================