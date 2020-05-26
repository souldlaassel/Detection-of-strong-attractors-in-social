import networkx as nx
import matplotlib.pyplot as plt

# import scipy as sp

# ================ Initialisation des Graph =================
# G = nx.karate_club_graph()
######################################
# G=nx.davis_southern_women_graph()
######################################
# G=nx.dodecahedral_graph()
######################################
G = nx.Graph()
G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
                  ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
                  ("C", "J"), ("C", "K")])
######################################

# ===========================================================

########## Degree Centrality #########
deg = {}
N = G.number_of_nodes()
for v in G:
    deg[v] = ((G.degree(v) / (N - 1)))

# print(deg)
# maxDeg = max(deg.values())
# print(maxDeg)
######################################

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
# G1 = G
# G1.remove_node('A')
# print(G.nodes())
# print(G1.nodes())
# print(G.nodes())
# //G.nodes()

####### Betweenness Centrality #######
between = {}
N = G.number_of_nodes()

between = {}
def betweenness():
    for v in G:
        print(v)
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

        print('segma_st_v: %s' % (segma_st_v))
        print('segma_st: %s' % (segma_st))
        if segma_st != 0:
            between[v] = segma_st_v / segma_st


# betweenness()
# print(between)
# print(nx.betweenness_centrality(G))
# maxBetween = max(between.values())

######################################

######## Coreness Centrality #########
# H = nx.Graph()
# H.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
#                   ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
#                   ("C", "J"), ("C", "K")])


corenessDict = dict([(v,0) for v in G])
def coreToPeri(H, n):
    if len(H) == 0:
        print("Stop")
        return 0
    for v in H:
        # print(v)
        if H.degree(v) <= n:
            print("is " + str(v) + " " + str(n))
            corenessDict[v] = n
            H.remove_node(v)
            return coreToPeri(H, n)
    coreToPeri(H, n + 1)


coreToPeri(G.copy(),1)
coreness = corenessDict
print(coreness)
maxCoreness = max(coreness.values())

######################################


##======== Affichage du réseau =======================
# dictR = close
# maxDictR = maxClose
dictR = coreness
maxDictR = maxCoreness
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
