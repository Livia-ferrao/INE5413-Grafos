from Grafo import Grafo

def floyd_warshall(file):
    grafo = Grafo(file)
    distance = grafo.matrizAdj()
    for k in range(grafo.dim):
        for i in range(grafo.dim):
            for j in range(grafo.dim):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
                distance[j][i] = distance[i][j]
    print_solution(distance)

def print_solution(distance):
    for i in range(len(distance)):
        print(f"{i}: ", end='')
        for j in range(len(distance)):
            print(distance[i][j], end=' ')
        print()

file = "../instancias/caminho_minimo/minimum.net"
floyd_warshall(file)


