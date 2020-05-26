import networkx as nx
import matplotlib.pyplot as plt

# ================ Initialisation des Graph =================
G = nx.Graph()
######################################
# G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
#                   ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
#                   ("C", "J"), ("C", "K")])
######################################
# G = nx.karate_club_graph()
######################################
# G = nx.read_gml('football.gml')
######################################
# G = nx.read_gml('lesmiserables.gml')
######################################
G = nx.read_gml('karate.gml')
######################################


nx.draw(G,with_labels=True)
# nx.draw_networkx(FG)

plt.show()