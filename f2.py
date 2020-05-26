import networkx as nx
import matplotlib.pyplot as plt
import queue
import random
import xlsxwriter
import collections
import numpy as np
# import ndlib.models.epidemics.SIRModel as sir
# import ndlib.models.ModelConfig as mc
# from bokeh.io import output_notebook, show
# from ndlib.viz.bokeh.DiffusionTrend import DiffusionTrend
# from ndlib.viz.bokeh.DiffusionPrevalence import DiffusionPrevalence
from networkx.algorithms.community import LFR_benchmark_graph

G = nx.Graph()
G.add_edges_from([("A", "D"), ("A", "I"), ("A", "C"), ("A", "E"), ("A", "F"), ("A", "H"),
                  ("B", "I"), ("B", "H"), ("B", "G"), ("B", "F"), ("B", "E"), ("B", "D"), ("B", "L"),
                  ("C", "J"), ("C", "K")])
#
# G = nx.read_gml('karate.gml')

# edges = nx.read_edgelist('dataset/amazon.txt')
# edges = nx.read_edgelist('dataset/Email-1133.txt')
# # edges = nx.read_edgelist('dataset/CA-Hep.txt')
# # edges = nx.read_edgelist('dataset/hamster.txt')
# # edges = nx.read_edgelist('dataset/PGP.txt')
# # edges = nx.read_edgelist('dataset/astro.txt')
# # edges = nx.read_edgelist('dataset/facebook.txt')
# G.add_edges_from(edges.edges())
# sir_res_stock = 'SIR_res.npy'
# # G=nx.read_edgelist("test.edgelist")
# print(edges)

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

# # ====== Remove non connected nodes ===========
# cv = list([c for c in sorted(nx.connected_components(G), key=len, reverse=True)])
# cv.remove(cv[0])
# for x in cv:
#     for z in x:
#         G.remove_node(z)
#
# print("Nodes: " + str(G.number_of_nodes()))
# print("Edges: " + str(G.number_of_edges()))
# print(nx.is_connected(G))
#
# nx.write_edgelist(G, "Email-1133.edgelist", data=False)
# fh=open("Email-1133.edgelist",'wb')
# nx.write_edgelist(G, fh, data=False)
# ==============================================

average_degree = ((2 * G.number_of_edges()) / G.number_of_nodes())
print("<k>: " + str(average_degree))

r=nx.degree_assortativity_coefficient(G)
print("r: " + str(r))

C = nx.average_clustering(G)
print("C: " + str(C))

# ls = []
# for v in G:
#     ls.append(nx.node_connected_component(G, v))
# cv = [len(c) for c in sorted(nx.strongly_connected_components(G), key=len, reverse=True)]
# print(cv[0].__len__())

# print(nx.isolates(G)[1])

# d = nx.average_shortest_path_length(G)
# print("d: " + str(d))
#
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


# print((1 / math.sqrt(max_degree)))
# print(1.5 * (1 / math.sqrt(max_degree)))


# G = nx.karate_club_graph()


# def sir_model_process(p=0.10, q=1, graph=G, u="A"):
#     # p = 0.10
#     # q = 1
#     # u = "NorthTexas"
#     I = []
#     I.insert(0, u)
#     # print(I)
#
#     S = {}
#     for v in graph:
#         S[v] = 1
#     S[u] = 2
#     # print(S)
#
#     R = []
#
#     count = 0
#
#     while I:
#         u = I.pop()
#         # print(I)
#         count = count + 1
#         for v in graph.neighbors(u):
#             if S[v] == 1:
#                 r = random.uniform(0, 1)
#                 # print(r)
#                 if r <= p:
#                     S[v] = 2
#                     # R[v] = 1
#                     # R.append(u)
#                     I.insert(0, v)
#                     # print(I)
#                 # end if
#             # end if
#         # end for
#         r = random.uniform(0, 1)
#         if r > q:
#             I.pop(0)
#         else:
#             R.append(u)
#     # end while
#
#     # res = {}
#
#     # res[1] = R
#     # res[2] = count
#
#     # print(R)
#     # print(len(R))
#     # print("count: " + str(count))
#     return R
#
#
# ########## Degree Centrality #########
# deg = {}
# N = G.number_of_nodes()
# for v in G:
#     deg[v] = ((G.degree(v) / (N - 1)))
#
# # print(deg)
# maxDeg = max(deg.values())
#
# # print(maxDeg)
# ######################################
#
# # def moyen(dict=deg, q=0.10):
# #     m = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
# #     s = 0
# #     r = q * dict.__len__()
# #     # print(r)
# #     # print(int(r))
# #     for x in range(int(r)):
# #         s = s + m[x][1]
# #     return s
#
#
# print("degree: " + str(sorted(deg.items(), key=lambda kv: kv[1], reverse=True)))
# # m = sorted(deg.items(), key=lambda kv: kv[1], reverse=True)
# # print(m)
# # print(moyen(dict=deg, q=0.10))
#
# SIR_res = {}
# for v in G:
#     res = []
#     counter = 0
#     # worksheet.write(row, col, v)
#     for x in range(100):
#         counter = counter + 1
#         res.append(sir_model_process(p=beta, graph=G, u=v).__len__())
#     # print(sum(res))
#     val = ((sum(res) / counter) / (N - 1))
#     # print(val)
#     SIR_res[v] = val
# np.save(sir_res_stock, SIR_res)
# # SIR_res = np.load('SIR_res.npy').item()
#
# print("SIR_res: " + str(sorted(SIR_res.items(), key=lambda kv: kv[1], reverse=True)))
#
#
# def moyen(dict1=deg, dict2=SIR_res, q=0.10):
#     m1 = sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)
#     s = 0
#     r = q * dict2.__len__()
#     # print(r)
#     # print(int(r))
#     for x in range(int(r)):
#         s = s + dict2[m1[x][0]]
#     return s
#
#
# def moyen_eff(dict=SIR_res, q=0.10):
#     m = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
#     s = 0
#     r = q * dict.__len__()
#     # print(r)
#     # print(int(r))
#     for x in range(int(r)):
#         s = s + m[x][1]
#     return s
#
#
# def eps(p=0.10, sp_eff_values = SIR_res, centr_values=deg):
#     val = 1 - (moyen(dict1=centr_values, dict2=sp_eff_values, q=p) / moyen_eff(dict=sp_eff_values, q=p))
#     # print(moyen(dict1=deg, dict2=sp_eff_values, q=p))
#     # print(moyen_eff(dict=sp_eff_values, q=p))
#     return val
#
#
# print(eps(p=0.05, sp_eff_values=SIR_res, centr_values=deg))
#
# def neighbor(benchmark, node, a, n, p):
#     if n <= 0 | n > 4:
#         return -1
#     value = benchmark[node]
#     if n == 1:
#         sum1 = 0
#         for j in G.neighbors(node):
#             sum1 = sum1 + a * benchmark[j]
#         value = value + sum1
#         return value
#     if n == 2:
#         sum1 = 0
#         if p is True:
#             print(str(node))
#         for j in G.neighbors(node):
#             if p is True:
#                 print(" " + str(j))
#             sum1 = sum1 + a * benchmark[j]
#             sum2 = 0
#             for l in G.neighbors(j):
#                 if l == node:
#                     continue
#                 if p is True:
#                     print("  " + str(l))
#                 sum2 = sum2 + (a ** 2) * benchmark[l]
#             value = value + sum2
#         value = value + sum1
#         return value
#     if n == 3:
#         sum1 = 0
#         if p is True:
#             print(str(node))
#         for j in G.neighbors(node):
#             if p is True:
#                 print(" " + str(j))
#             sum1 = sum1 + a * benchmark[j]
#             sum2 = 0
#             for l in G.neighbors(j):
#                 if l == node:
#                     continue
#                 if p is True:
#                     print("  " + str(l))
#                 sum2 = sum2 + (a ** 2) * benchmark[l]
#                 sum3 = 0
#                 for m in G.neighbors(l):
#                     if m == j:
#                         continue
#                     if p is True:
#                         print("   " + str(m))
#                     sum3 = sum3 + (a ** 3) * benchmark[m]
#                 value = value + sum3
#             value = value + sum2
#         value = value + sum1
#         return value
#     if n == 4:
#         sum1 = 0
#         if p is True:
#             print(str(node))
#         for j in G.neighbors(node):
#             if p is True:
#                 print(" " + str(j))
#             sum1 = sum1 + a * benchmark[j]
#             sum2 = 0
#             for l in G.neighbors(j):
#                 if l == node:
#                     continue
#                 if p is True:
#                     print("  " + str(l))
#                 sum2 = sum2 + (a ** 2) * benchmark[l]
#                 sum3 = 0
#                 for m in G.neighbors(l):
#                     if m == j:
#                         continue
#                     if p is True:
#                         print("   " + str(m))
#                     sum3 = sum3 + (a ** 3) * benchmark[m]
#                     sum4 = 0
#                     for s in G.neighbors(m):
#                         if s == l:
#                             continue
#                         if p is True:
#                             print("    " + str(s))
#                         sum4 = sum4 + (a ** 4) * benchmark[m]
#                     value = value + sum4
#                 value = value + sum3
#             value = value + sum2
#         value = value + sum1
#         return value
#
#
# neighbor_values = {}
# for v in G:
#     t = neighbor(benchmark=nx.degree_centrality(G),node=v,a=0.2,n=1, p=False)
#     neighbor_values[v] = t
#     # print(str(v) + " " + str(t))
#
# print(neighbor_values)
#
# ####################################################################################
# diag_val = {}
# for x in range(1,20):
#     i = x * 0.01
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=deg)
#
# plt.plot(diag_val.keys(), diag_val.values(), label='k', color='black', linestyle='solid', marker='s')
# #####################################################################################
# diag_val = {}
# for x in range(1,20):
#     i = x * 0.01
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_values)
#
# plt.plot(diag_val.keys(), diag_val.values(), label='C¹(k)', color='red', linestyle='solid', marker='o')
# #####################################################################################
# neighbor_values = {}
# for v in G:
#     t = neighbor(benchmark=nx.degree_centrality(G),node=v,a=0.2,n=2, p=False)
#     neighbor_values[v] = t
#     # print(str(v) + " " + str(t))
# diag_val = {}
# for x in range(1,20):
#     i = x * 0.01
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_values)
# print(neighbor_values)
# plt.plot(diag_val.keys(), diag_val.values(), label='C²(k)', color='blue', linestyle='solid', marker='^')
# #######################################################################################
# neighbor_values = {}
# for v in G:
#     t = neighbor(benchmark=nx.degree_centrality(G),node=v,a=0.2,n=3, p=False)
#     neighbor_values[v] = t
#     # print(str(v) + " " + str(t))
# diag_val = {}
# for x in range(1,20):
#     i = x * 0.01
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_values)
# print(neighbor_values)
# plt.plot(diag_val.keys(), diag_val.values(), label='C³(k)', color='c', linestyle='solid', marker='v')
# #######################################################################################
# neighbor_values = {}
# for v in G:
#     t = neighbor(benchmark=nx.degree_centrality(G),node=v,a=0.2,n=4, p=False)
#     neighbor_values[v] = t
#     # print(str(v) + " " + str(t))
# diag_val = {}
# for x in range(1,20):
#     i = x * 0.01
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_values)
# print(neighbor_values)
# plt.plot(diag_val.keys(), diag_val.values(), label='C⁴(k)', color='fuchsia', linestyle='solid', marker='<')
# #######################################################################################
# plt.xlabel('p')
# plt.ylabel('ε(p)')
# plt.title("Email")
# plt.legend()
# plt.axis([0.0, 0.20, 0.0, 0.06])
# plt.show()

# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('karate_SIR_Model.xlsx')
# worksheet = workbook.add_worksheet()
#
# # Start from the first cell. Rows and columns are zero indexed.
# row = 0
# col = 0
#
# for v in G:
#     worksheet.write(row, col, v)
#     row += 1
#
# tab = {}
# for col in range(20):
#     row = 0
#     for v in G:
#         res = []
#         counter = 0
#         # worksheet.write(row, col, v)
#         for x in range(100):
#             counter = counter + 1
#             res.append(sir_model_process(p=0.22, q=1, graph=G, u=v).__len__())
#         print(sum(res))
#         val = (sum(res)/counter)
#         # print(val)
#         tab[v] = val
#         worksheet.write(row, col + 1, val)
#         row += 1
#
# print(tab)
# sorted_by_value = sorted(tab.items(), key=lambda kv: kv[1], reverse=True)
# print(sorted_by_value)
#
# workbook.close()

# Network topology
# G = nx.erdos_renyi_graph(110, 0.1)

# n = 250
# tau1 = 3
# tau2 = 1.5
# mu = 0.1
# G = LFR_benchmark_graph(n, tau1, tau2, mu, average_degree=5,
#                        min_community=20, seed=10)

# G

# # Model Selection
# model = sir.SIRModel(G)
#
# # Model Configuration
# config = mc.Configuration()
# config.add_model_parameter('beta', 0.001)
# config.add_model_parameter('gamma', 0.01)
# config.add_model_parameter("percentage_infected", 0.05)
# model.set_initial_status(config)
#
# # Simulation
# iterations = model.iteration_bunch(200)
# trends = model.build_trends(iterations)
#
# viz = DiffusionTrend(model, trends)
# p = viz.plot(width=400, height=400)
# show(p)
#
# viz2 = DiffusionPrevalence(model, trends)
# p2 = viz2.plot(width=400, height=400)
# show(p2)


# G.remove_node('C')

# nx.draw(G,with_labels=True)
# plt.show()
# coreness = {}
# def core(G,n):
#     if len(G) == 0:
#         print("Stop")
#         return 0
#     for v in G:
#         print(v)
#         if G.degree(v) <= n:
#             print("is " + str(v) + " " + str(n))
#             coreness[v] = n
#             G.remove_node(v)
#             return core(G,n)
#     core(G,n+1)
#
# core(G,1)
# print(coreness)

# print(G.number_of_edges())

# nx.draw(G, with_labels=False)
# plt.show()
