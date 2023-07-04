import math
from Grafo import Grafo


def busca_largura(file, s: int):
    s -= 1
    grafo = Grafo(file)

    visted = [False] * grafo.qtdVertices() # Vertices já visitados
    distance = [math.inf] * grafo.qtdVertices()  # Distância dos vértices do inicial
    predecessors = [None] * grafo.qtdVertices()  # Vertice antecessor aos vertices

    visted[s] = True # Marca o vertice de origem como já visitado...
    distance[s] = 0    # Distancia inicial igual a 0
    
    Q = [s]     # Fila de visitas - inicia com S

    while Q:
        u = Q.pop(0)
        for v in grafo.vizinhos(u+1):
            i = grafo.nodes.index(v)
            if not visted[i]:
                visted[i] = True
                distance[i] = distance[u] + 1
                predecessors[i] = u
                Q.append(i)

    # print resultado das distancias
    for i in range(max(distance)+1):
        print(f"{i}: ", end='')
        for vertice, distancia in enumerate(distance):
            if distancia == i:
                print(vertice + 1, end=' ')
        print()

file = "../instancias/caminho_minimo/fln_pequena.net"
s = 1
busca_largura(file, s)
