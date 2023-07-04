import math
from Grafo import Grafo

# file = "../instancias/dirigidos/dirigido2.net"
file = "../instancias/dirigidos/dirigido1.net"

def main(file):
    G = Grafo(file)
    A = stronglyConnectedComponents(G)
    forest = getForest(A)
    printForest(forest)


def stronglyConnectedComponents(G):
    _, _, _, F = DFS(G)
    G.getTransposedGraph()
    _, _, At, _ = DFS_adapted(G, F)
    return At


def DFS(G: Grafo):
    qtdVertices = G.qtdVertices()
    C = [False] * qtdVertices
    T = [math.inf] * qtdVertices
    F = [math.inf] * qtdVertices
    A = [None] * qtdVertices

    time = 0
    for u in range(qtdVertices):
        if (C[u] == False):
            time = DFSVisit(G, u, C, T, A, F, time)

    return (C, T, A, F)


def DFS_adapted(G: Grafo, F1: list[int]):
    qtdVertices = G.qtdVertices()
    C = [False] * qtdVertices
    T = [math.inf] * qtdVertices
    F = [math.inf] * qtdVertices
    A = [None] * qtdVertices

    time = 0
    # Lista dos vértices em ordem descrencente em relação ao F
    orderedNodes = [x for x in range(qtdVertices)]
    orderedNodes.sort(reverse=True, key=lambda x: F1[x])

    for u in orderedNodes:
        if (C[u] == False):
            time = DFSVisit(G, u, C, T, A, F, time)

    return (C, T, A, F)


def DFSVisit(G: Grafo, v: int, C: list[bool], T: list[int], A: list[int], F: list[int], time):
    C[v] = True
    time += 1
    T[v] = time

    for u in G.vizinhos(v+1):
        i = G.nodes.index(u)
        if C[i] == False:
            A[i] = v
            time = DFSVisit(G, i, C, T, A, F, time)
    
    time += 1
    F[v] = time
    return time

def getForest(A: list[int]):
    numVertices = len(A)
    indexTree = [None] * numVertices
    maxIndex = 0
    forest = []

    for i in range(numVertices):
        if indexTree[i] == None:
            predecessor = A[i]
            tree = [i]

            while True:
                if predecessor == None:
                    for node in tree:
                        indexTree[node] = maxIndex
                    forest.append(tree)
                    maxIndex += 1
                    break

                predecessorIndexTree = indexTree[predecessor]
                if predecessorIndexTree != None:
                    for u in tree:
                        indexTree[u] = predecessorIndexTree
                    forest[predecessorIndexTree] += tree
                    break

                tree.append(predecessor)
                predecessor = A[predecessor]
    return forest


def printForest(forest):
    for tree in forest:
        treeStr = ""
        for v in tree:
            treeStr += str(v+1) + ','
        print(treeStr[:-1])


main(file)
