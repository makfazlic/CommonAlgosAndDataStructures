import sys
V = []                          # vertexes 
Adj = []                        # adjacency list
V_idx = {}                      # index: name --> vertex_id

#
# Exercise: read a graph from the input in the following format:
#
# v | Adj(v)
# ------------
# TI VS UR GR
# UR TI GR VS
# GR TI UR
# VS TI



def dfs():
    n = len(V)
    P = [None]*n
    D = [None]*n
    F = [None]*n
    t = 0
    S = []
    for i in range(n):
        if D[i] == None:
            S.append(i)
            P[i] = None
            while len(S) > 0:
                v = S[-1]
                if D[v] == None:
                    D[v] = t
                    t += 1
                    for w in Adj[v]:
                        S.append(w)
                        P[w] = v
                else:
                    if F[v] == None:
                        F[v] = t
                        t += 1
                    del S[-1]
    return P, D, F

for line in sys.stdin.readlines():
    A = line.strip().split()
    for v in A:
        # v is a string, vertex name
        if v not in V_idx:
            V_idx[v] = len(V)
            V.append(v)
            Adj.append([])
    v_i = V_idx[A[0]]
    for i in range(1,len(A)):
        u_i = V_idx[A[i]]
        Adj[u_i].append(v_i)
        Adj[v_i].append(u_i)



        
P, D, F = dfs()
for i in range(len(V)):
    if P[i] == None:
        print(V[i], "itself" ,D[i], F[i])
    else:
        print(V[i], V[P[i]] ,D[i], F[i])