from Grafo import Grafo

file = "../instancias/dirigidos/manha.net"

def main(file):
    G = Grafo(file) 
    O = Ordenacao_topologica(G)
    print(O)

def Ordenacao_topologica(G):
    #Criar listas para todos os vértices
    qtdVertices = G.qtdVertices()
    C = [False for i in range(qtdVertices)]
    T = [float('inf') for i in range(qtdVertices)]
    F = [float('inf') for i in range(qtdVertices)]

    tempo = 0

    #lista vértices ordenados topologicamente
    O = []

    #Visita vértices 
    for u in range(qtdVertices-1): #andar ao contrario??
        if not C[u]:
            DFS_visit_OT(G, u+1, C, T, F, tempo, O)
    
    return '→'.join(O)

def DFS_visit_OT(G, v, C, T, F, tempo, O):

    C[v-1] = True
    tempo += 1
    T[v-1] = tempo

    for u in G.vizinhos_index(v):
        if not C[u-1]:
            DFS_visit_OT(G, u, C, T, F, tempo, O)

    tempo += 1
    F[v-1] = tempo

    #Adiciona o rotulo do vértice u no início da lista O
    O.insert(0,G.rotulo(v))

main(file)