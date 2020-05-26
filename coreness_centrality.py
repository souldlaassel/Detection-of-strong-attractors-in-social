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
# G = nx.read_gml('football.gml')
# ===========================================================

######## Coreness Centrality #########
# H = nx.Graph()
# H.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
#                   ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
#                   ("C", "J"), ("C", "K")])


corenessDict = dict([(v,0) for v in G])
def coreToPeri(H, n):
    if len(H) == 0:
        # print("Stop")
        return 0
    for v in H:
        # print(v)
        if H.degree(v) <= n:
            # print("is " + str(v) + " " + str(n))
            corenessDict[v] = n
            # print(str(v) + ": " + str(n))
            H.remove_node(v)
            return coreToPeri(H, n)
    coreToPeri(H, n + 1)
#
# def coreToPeri(H, n):
#     while(len(H)!=0):
#         for v in H:
#             print(v)
#             if H.degree(v) <= n:
#                 corenessDict[v] = n
#                 print(str(v) + ": " + str(n))
#                 H.remove_node(v)
#         n = n + 1

dict = nx.core_number(G)
print(dict)
print(G.number_of_nodes())
coreToPeri(G.copy(),1)
print(corenessDict)
coreness = dict
# print(coreness)
maxCoreness = max(coreness.values())

######################################

##======== Affichage du réseau =======================
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