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

######## Neighborhood Centrality #########

neighbor = {}
# def neighbor(graph, benchmark, node, a, n):
#     value = 0
#     value = benchmark[node]
#     helpNode = node
#     for x in range(1, n):
#         print("  "+str(x))
#         sumTeta = 0
#         for nei in G.neighbors(helpNode):
#             print(nei)
#             sumTeta = sumTeta + benchmark[nei]
#         value = value + (a**x)*sumTeta
#         helpNode

# H = G.copy()
# value = 0
# coef = {}
# def Rec(benchmark, node, n, a, p):
#     # if n == 0:
#     #     return benchmark[node]
#     if n == 1:
#         sumTeta = benchmark[node]
#         for j in G.neighbors(node):
#             sumTeta = sumTeta + benchmark[j]
#         return sumTeta
#     else:
#         sumTeta = 0
#         G.remove_node(node)
#         for j in G.neighbors(node):
#             # sumTeta = sumTeta + benchmark[j]
#             sumTeta = sumTeta + Rec(benchmark, j, n-1, a, p+1)
#             # Rec(benchmark, j, n-1, a, p+1)
#         # value = value + (a ** p) * sumTeta
#
# # Rec(teta, i, 4, a, 0)

# myList = ["prem",4,2,3,"sai",2,3,1]
# myList.remove(4)
# print(myList)



def neighbor(graph, benchmark, node, a, n):
    value = benchmark[node]
    for i in G:
        if node != i:
            sp = nx.all_shortest_paths(G, node, i)
            for p in sp:
                # if(len(p) <= n+1):
                if(len(p) == n+1):
                    # print(p)
                    sum = 0
                    for x in range(1,n+1):
                        if(x < len(p)) :
                            sum = sum + (a ** x) * benchmark[p[x]]
                            # print(str(x) + " " + p[x])
                    # print(x)
                    value = value + sum
    return value

def neighbor2(benchmark, node, a, n, p):
    if n <= 0 | n > 4:
        return -1
    value = benchmark[node]
    if n == 1:
        sum1 = 0
        for j in G.neighbors(node):
            sum1 = sum1 + a * benchmark[j]
        value = value + sum1
        return value
    if n == 2:
        sum1 = 0
        if p is True:
            print(str(node))
        for j in G.neighbors(node):
            if p is True:
                print(" " + str(j))
            sum1 = sum1 + a * benchmark[j]
            sum2 = 0
            for l in G.neighbors(j):
                if l == node:
                    continue
                if p is True:
                    print("  " + str(l))
                sum2 = sum2 + (a ** 2) * benchmark[l]
            value = value + sum2
        value = value + sum1
        return value
    if n == 3:
        sum1 = 0
        if p is True:
            print(str(node))
        for j in G.neighbors(node):
            if p is True:
                print(" " + str(j))
            sum1 = sum1 + a * benchmark[j]
            sum2 = 0
            for l in G.neighbors(j):
                if l == node:
                    continue
                if p is True:
                    print("  " + str(l))
                sum2 = sum2 + (a ** 2) * benchmark[l]
                sum3 = 0
                for m in G.neighbors(l):
                    if m == j:
                        continue
                    if p is True:
                        print("   " + str(m))
                    sum3 = sum3 + (a ** 3) * benchmark[m]
                value = value + sum3
            value = value + sum2
        value = value + sum1
        return value
    if n == 4:
        sum1 = 0
        if p is True:
            print(str(node))
        for j in G.neighbors(node):
            if p is True:
                print(" " + str(j))
            sum1 = sum1 + a * benchmark[j]
            sum2 = 0
            for l in G.neighbors(j):
                if l == node:
                    continue
                if p is True:
                    print("  " + str(l))
                sum2 = sum2 + (a ** 2) * benchmark[l]
                sum3 = 0
                for m in G.neighbors(l):
                    if m == j:
                        continue
                    if p is True:
                        print("   " + str(m))
                    sum3 = sum3 + (a ** 3) * benchmark[m]
                    sum4 = 0
                    for s in G.neighbors(m):
                        if s == l:
                            continue
                        if p is True:
                            print("    " + str(s))
                        sum4 = sum4 + (a ** 4) * benchmark[m]
                    value = value + sum4
                value = value + sum3
            value = value + sum2
        value = value + sum1
        return value


# def neighborhood(G, node, n):
#     path_lengths = nx.dijkstra_path(G, node)
#     print(path_lengths)
#     # return [node for node, length in path_lengths.iteritems()
#     #                 if length == n]

# print(neighborhood(G, "A", 1))
# ['v2', 'v3']
# print(neighborhood(G, 'B', 2))
# ['v4']

# for v in G:
#     t = neighbor(graph=G,benchmark=nx.degree_centrality(G),node=v,a=0.2,n=3)
#     print(v + " " + str(t))

myList = []
for v in G:
    t = neighbor2(benchmark=nx.degree_centrality(G),node=v,a=0.2,n=4, p=False)
    myList.append(t)
    # print(str(v) + " " + str(t))

myList.sort()
print(myList)

# printeighbor(graph=G,benchmark=nx.degree_centrality(G),node="I",a=0.2,n=2)
# print(" " + str(t))


# sp = nx.all_shortest_paths(G, "A", "B")
# for p in sp:
#     print(p)
# print(nx.all_shortest_paths(G, "A", "D"))
# path_lengths = nx.single_source_dijkstra_path_length(G, "A")
# print(path_lengths)
nx.draw(G,with_labels=True)
# nx.draw_networkx(FG)

plt.show()







######################################