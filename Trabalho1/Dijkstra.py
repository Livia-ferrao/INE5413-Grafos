from Grafo import Grafo
import math

file = "../instancias/caminho_minimo/fln_pequena.net"

def main():
    grafo = Grafo(file)
    distance, predecessors = dijkstra(grafo, 2)
    printPaths(distance, predecessors)

def dijkstra(grafo: Grafo, s: int):
    s = s - 1
    distance = [math.inf] * grafo.qtdVertices()
    predecessors = [-1] * grafo.qtdVertices()
    visited = [False] * grafo.qtdVertices()
    distance[s] = 0

    while not all(visited):
        u = -1
        for i in range(grafo.qtdVertices()):
            if (visited[i] == False) and (distance[i] < distance[u] or u == -1):
                u = i
        visited[u] = True

        for v in grafo.vizinhos(u+1):
            i = grafo.nodes.index(v)
            if not visited[i]:
                peso_uv = grafo.peso(u+1, i+1)
                if distance[i] > distance[u] + peso_uv:
                    distance[i] = distance[u] + peso_uv
                    predecessors[i] = u
    return distance, predecessors

def printPaths(distance, predecessors):
    for v in range(len(distance)):
        print(v+1, ": ", sep="", end="")

        path = [v]
        a = predecessors[v]
        while a != -1:
            path.append(a)
            a = predecessors[a]

        pathLen = len(path)
        for index, i in enumerate(path[::-1]):
            print(i+1, end='')
            if index != pathLen-1:
                print(",", end="")

        print("; d=", distance[v], sep="")

main()