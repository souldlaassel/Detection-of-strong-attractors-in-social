import networkx as nx
import matplotlib.pyplot as plt
import queue
import random
import xlsxwriter
import collections
import numpy as np
import sys

G = nx.Graph()

G=nx.read_edgelist("dataset/Email-1133.edgelist")
sir_res_stock = 'SIR_Data/SIR_Email.npy'
beta = 0.08
dataset = 'Email'
# ========================================
# G=nx.read_edgelist("dataset/CA-Hep.edgelist")
# sir_res_stock = 'SIR_Data/SIR_CA_Hep.npy'
# beta = 0.12
# dataset = 'CA_Hep'
# ========================================
# G=nx.read_edgelist("dataset/hamster.edgelist")
# sir_res_stock = 'SIR_Data/SIR_hamster.npy'
# beta = 0.04
# dataset = 'hamster'
# ========================================
# G=nx.read_edgelist("dataset/PGP.edgelist")
# sir_res_stock = 'SIR_Data/SIR_PGP.npy'
# beta = 0.08
# dataset = 'PGP'
# ========================================
# G=nx.read_edgelist("dataset/astro.edgelist")
# sir_res_stock = 'SIR_Data/SIR_astro.npy'
# beta = 0.023
# dataset = 'astro'
# ========================================
# G=nx.read_edgelist("dataset/facebook.edgelist")
# sir_res_stock = 'SIR_Data/SIR_facebook.npy'
# beta = 0.014
# dataset = 'facebook'
# ========================================
SIR_res = np.load(sir_res_stock).item()
neighbor_degree_values = np.load('Data/' + dataset + '/neighborhood2_degree.npy').item()
neighbor_coreness_values = np.load('Data/' + dataset + '/neighborhood2_coreness.npy').item()
coreness = np.load('Data/'+dataset+'/coreness.npy').item()
deg = np.load('Data/'+dataset+'/degree.npy').item()
eigenvect = np.load('Data/'+dataset+'/eigenvector.npy').item()
close = np.load('Data/'+dataset+'/closeness.npy').item()
between = np.load('Data/'+dataset+'/betweenness.npy').item()
# ==================================================

########## Degree Centrality #########
# deg = {}
# N = G.number_of_nodes()
# for v in G:
#     deg[v] = ((G.degree(v) / (N - 1)))

# print(deg)
# maxDeg = max(deg.values())



# print("degree: " + str(sorted(deg.items(), key=lambda kv: kv[1], reverse=True)))

# =============================================

# print("SIR_res: " + str(sorted(SIR_res.items(), key=lambda kv: kv[1], reverse=True)))


def moyen(dict1=deg, dict2=SIR_res, q=0.10):
    m1 = sorted(dict1.items(), key=lambda kv: kv[1], reverse=True)
    s = 0
    r = q * dict2.__len__()
    # print(r)
    # print(int(r))
    for x in range(int(r)):
        s = s + dict2[m1[x][0]]
    return s


def moyen_eff(dict=SIR_res, q=0.10):
    m = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    s = 0
    r = q * dict.__len__()
    # print(r)
    # print(int(r))
    for x in range(int(r)):
        s = s + m[x][1]
    return s


def eps(p=0.10, sp_eff_values = SIR_res, centr_values=deg):
    val = 1 - (moyen(dict1=centr_values, dict2=sp_eff_values, q=p) / moyen_eff(dict=sp_eff_values, q=p))
    # print(moyen(dict1=deg, dict2=sp_eff_values, q=p))
    # print(moyen_eff(dict=sp_eff_values, q=p))
    return val


print(eps(p=0.05, sp_eff_values=SIR_res, centr_values=deg))

def neighbor(benchmark, node, a, n, p):
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




####################################################################################
pas = 0.01
###################################################################################
print("Degree Processing...")
# =======================================================
# np.save('Data/'+dataset+'/degree.npy', deg)
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=deg)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='deg', color='black', linestyle='solid', marker='s')
print("Degree Done!")
#####################################################################################
print("Coreness Processing...")
G.remove_edges_from(nx.selfloop_edges(G))
print(G.number_of_nodes())
print(G.number_of_edges())
# =======================================================
# coreness = nx.core_number(G)
# np.save('Data/'+dataset+'/coreness.npy', coreness)
# =======================================================
print("Coreness diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=coreness)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='kshell', color='red', linestyle='solid', marker='o')
print("Coreness Done!")
#####################################################################################
print("Eigenvector Processing...")
# =======================================================
# eigenvect = nx.eigenvector_centrality(G)
# np.save('Data/'+dataset+'/eigenvector.npy', eigenvect)
# =======================================================
print("Eigenvector diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=eigenvect)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='eig', color='maroon', linestyle='solid', marker='v')
print("Eigenvector Done!")
#####################################################################################
# print("Eccentricity Processing...")
# eccent = nx.eccentricity(G)
# print(eccent)
# print("Eccentricity diag Processing...")
# diag_val = {}
# for x in range(1,20):
#     i = x * pas
#     diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=eccent)
#
# plt.plot(diag_val.keys(), diag_val.values(), label='eccent', color='fuchsia', linestyle='solid', marker='<')
# print("Eccentricity Done!")
#####################################################################################
print("Closeness Processing...")
# =======================================================
# close = nx.closeness_centrality(G)
# np.save('Data/'+dataset+'/closeness.npy', close)
# =======================================================
print("Closeness diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=close)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='close', color='fuchsia', linestyle='solid', marker='<')
print("Closeness Done!")
#####################################################################################
print("Betweenness Processing...")
# =======================================================
# between = nx.betweenness_centrality(G)
# np.save('Data/'+dataset+'/betweenness.npy', between)
# =======================================================
print("Betweenness diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=between)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='betw', color='darkorange', linestyle='solid', marker='>')
print("Betweenness Done!")
#####################################################################################
print("Neighborhood 2 Degree Processing...")
# =======================================================
# neighbor_degree_values = {}
# # ===================
# for v in G:
#     t = neighbor(benchmark=deg,node=v,a=0.2,n=2, p=False)
#     neighbor_degree_values[v] = t
#     # print(str(v) + " " + str(t))
# # ===================
# np.save('Data/' + dataset + '/neighborhood2_degree.npy', neighbor_degree_values)
# =======================================================
print("Neighborhood 2 Degree diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_degree_values)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='nghd2Deg', color='blue', linestyle='solid', marker='^')
print("Neighborhood 2 Degree Done!")
#####################################################################################
print("Neighborhood 2 Coreness Processing...")
# =======================================================
# neighbor_coreness_values = {}
# # ===================
# for v in G:
#     t = neighbor(benchmark=coreness,node=v,a=0.2,n=2, p=False)
#     neighbor_coreness_values[v] = t
#     # print(str(v) + " " + str(t))
# # ===================
# np.save('Data/' + dataset + '/neighborhood2_coreness.npy', neighbor_coreness_values)
# =======================================================
print("Neighborhood 2 Coreness diag Processing...")
# =======================================================
diag_val = {}
for x in range(1,20):
    i = x * pas
    diag_val[i] = eps(p=i, sp_eff_values=SIR_res, centr_values=neighbor_coreness_values)
# =======================================================
plt.plot(diag_val.keys(), diag_val.values(), label='nghd2Kshell', color='gray', linestyle='solid', marker='D')
print("Neighborhood 2 Coreness Done!")
#######################################################################################

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
#######################################################################################
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
#######################################################################################
plt.xlabel('p')
plt.ylabel('ε(p)')
plt.title(dataset)
plt.legend()
plt.axis([0.0, 0.20, 0.0, 0.5])
plt.show()

# # Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('karate_SIR_Model.xlsx')
# worksheet = workbook.add_worksheet()
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
# ========================================