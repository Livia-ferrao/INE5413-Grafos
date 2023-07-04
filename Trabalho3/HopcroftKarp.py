from math import inf
from Grafo import Grafo

def main(file):
    G = Grafo(file) 
    M = hopcroft_karp(G)
    print(M)

def hopcroft_karp(G):
    pair_u = {u: None for u in G.X}
    pair_v = {v: None for v in G.Y}
    dist = {None: float("inf")}
    matching = 0

    while bfs(G, pair_u, pair_v, dist):
        for u in G.X:
            if pair_u[u] is None and dfs(G, u, pair_u, pair_v, dist):
                matching += 1

    return matching, pair_u


def bfs(G, pair_u, pair_v, dist):
    queue = []
    for x in G.X:
        if pair_u[x] is None:
            dist[x] = 0
            queue.append(x)
        else:
            dist[x] = float("inf")

    dist[None] = float("inf")

    while queue:
        x = queue.pop(0)
        if x != None:
            x_index = G.getIndex(x)
            #print(x_index)
            if dist[x] < dist[None]:
                for y in G.getVizinhos(x_index):
                    #print(G.vizinhos(x_index))
                    if dist[pair_v[y]] == float("inf"):
                        dist[pair_v[y]] = dist[x] + 1
                        queue.append(pair_v[y])

    return dist[None] != float("inf")


def dfs(G, x, pair_u, pair_v, dist):
    if x is not None:
        x_index = G.getIndex(x)
        for y in G.getVizinhos(x_index):
            if dist[pair_v[y]] == dist[x] + 1 and dfs(G, pair_v[y], pair_u, pair_v, dist):
                pair_v[y] = x
                pair_u[x] = y
                return True

        dist[x] = float("inf")
        return False
    return True

file = "../instancias/emparelhamento_maximo/pequeno.net"
main(file)
