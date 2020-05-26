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
G = nx.Graph()
G.add_edges_from([("A", "B"), ("A", "E"), ("A", "C"),
                  ("B", "C"), ("B", "E"), ("B", "G"), ("B", "H"),
                  ("C", "D"), ("C", "E"),
                  ("D", "E"), ("D", "F"), ("D", "G"),
                  ("E", "G"),
                  # ("F", "G"),
                  ("G", "H"), ("H", "I"), ("I", "J")])
######################################

# ===========================================================

######## Closeness Centrality ########
close = {}
N = G.number_of_nodes()
for v in G:
    sp = nx.shortest_path(G, source=v)
    sp.pop(v, None)
    totalsp = sum([len(value) - 1 for value in sp.values()])
    close[v] = (N - 1) / totalsp

maxClose = max(close.values())
# print("close1")
# print(close)
# print(maxClose)
# print("close2")
# print(nx.closeness_centrality(G))
######################################

##======== Affichage du réseau =======================
dictR = close
maxDictR = maxClose
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
                       node_color='r',
                       node_size=[(i / maxDictR) * 2000 for i in list(dictR.values())],
                       alpha=0.9)
nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.8)
nx.draw_networkx_labels(G, posI, labels, font_size=8)
# nx.draw_networkx(G)
plt.axis('off')
plt.show()
# ===================================================