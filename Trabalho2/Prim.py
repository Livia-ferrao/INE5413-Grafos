from Grafo import Grafo
import math

file = "../instancias/arvore_geradora_minima/agm_tiny.net"

def main(file):
    grafo = Grafo(file)
    
    total_edges_weight, connections = Prim(grafo)
    
    print (total_edges_weight)
    last_node = connections[list(connections.keys())[-1]][-1]   #Tudo isso pra não ter uma vírgula no final...
    for starter_node in connections:
        for end_node in connections[starter_node]:
            print (str(grafo.nodes.index(starter_node)) + "-" + str(grafo.nodes.index(end_node)), end="")
            if end_node != last_node:
                print (", ", end="")
    print()

# Retorna o peso e as conexões da árvore geradora mínima       
def Prim(grafo):
    connections = {}
    total_edges_weight = 0
    visited_nodes = []
    visited_nodes.append(grafo.nodes[0])
    
    # Repete a iteração enquanto a lista de nós visitados não for igual aos nós do grafo
    while set(visited_nodes) != set(grafo.nodes):
        connection, cheapest_weight = get_cheapest_connected_connection(visited_nodes, grafo)
        
        # Adiciona a nova conexão no dicionário de conexões e atualiza os nós visitados e o peso total
        starter_node = list(connection.keys())[0]
        end_node = list(connection.values())[0]
        if starter_node in connections:
            connections[starter_node].append(end_node)
        else:
            connections[starter_node] = [end_node]
        
        total_edges_weight += cheapest_weight
        visited_nodes.append(end_node)
    
    return total_edges_weight, connections

# Retorna o peso da conexão de menor custo entre os nós visitados e os nós envolvidos nessa conexão
def get_cheapest_connected_connection(visited_nodes, grafo):
    cheapest_weight = math.inf
    
    # Checa cada aresta conectada a cada nó visitado, ignorando caso seja entre dois nós visitados selecionando a de menor custo
    for node in visited_nodes:
        for vizinho in grafo.vizinhos(1 + grafo.nodes.index(node)):
            if vizinho not in visited_nodes:
                weight = grafo.peso(1 + grafo.nodes.index(node), 1 + grafo.nodes.index(vizinho))
                if weight < cheapest_weight:
                    cheapest_weight = weight
                    connection = {node : vizinho}
                    
    return connection, cheapest_weight


main(file)


