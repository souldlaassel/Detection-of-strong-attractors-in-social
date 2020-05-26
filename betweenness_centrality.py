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
G = nx.read_gml('football.gml')

# ===========================================================

####### Betweenness Centrality #######
between = {}
N = G.number_of_nodes()

between = {}
def betweenness():
    for v in G:
        # print(v)
        segma_st = 0
        segma_st_v = 0
        help = []
        for s in G:
            for t in G:
                if (t, s) in help:
                    continue
                help.append((s, t))
                sp = nx.all_shortest_paths(G, source=s, target=t)
                if v == s or v == t:
                    continue
                elif s == t:
                    segma_st = segma_st + 1
                    continue
                else:
                    for p in sp:
                        segma_st = segma_st + 1
                        # print(p)
                        if v in p:
                            segma_st_v = segma_st_v + 1
                            # print(p)

        # print('segma_st_v: %s' % (segma_st_v))
        # print('segma_st: %s' % (segma_st))
        if segma_st != 0:
            between[v] = segma_st_v / segma_st


betweenness()
# print(between)
# print(nx.betweenness_centrality(G))
maxBetween = max(between.values())

######################################

##======== Affichage du réseau =======================
dictR = between
maxDictR = maxBetween
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