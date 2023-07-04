from Grafo import Grafo

def ciclo_euleriano(file):
    ini_node = 0
    grafo = Grafo(file)

    main_cycle = []
    sub_cycle = []

    # Cria um dicionário para listar as arestas visitadas entre cada vértice 
    visited_edges = {}
    for node in grafo.nodes:
        visited_edges[node] = []

    # Muda o nó caso ele não faça parte de uma área conectada
    current_node = grafo.nodes[ini_node]
    while len(grafo.vizinhos(1 + grafo.nodes.index(current_node))) <= 0:
        for node in grafo.nodes:
            if len(grafo.vizinhos(1 + grafo.nodes.index(node))) > 0:
                current_node = node
                break

    main_cycle.append(grafo.nodes[ini_node])
    is_eu_cycle = True

    # Percorre o grafo até que todos os vértices tenham sido visitados 
    while is_eu_cycle:    
        
        current_node, node_index = get_linked_node_with_unvisited_edge(main_cycle, visited_edges, grafo)   
        
        # Se não retornar nenhum nó checa para ver algum dos nós não conectados tem vizinhos e quebra
        if current_node == None:    
            break

        # Começa o próximo subciclo
        sub_cycle, is_eu_cycle = get_next_sub_cycle(grafo, visited_edges, current_node)

        # Adiciona o subciclo no ciclo principal
        for i in range (1, len(sub_cycle)):
            main_cycle.insert(node_index + i, sub_cycle[i])

    return is_eu_cycle

# Da lista de vértices já percorridos, retorna o que ainda tem alguma vértice a visitar e a posição dele na lista pricipal
def get_linked_node_with_unvisited_edge(main_cycle, visited_edges, grafo):
    node_index = 0 
    for node in main_cycle: 
        for adjacent_node in grafo.vizinhos(1 + grafo.nodes.index(node)): 
            if adjacent_node not in visited_edges[node]: 
                return node, node_index
        node_index += 1
    
    return None, 0

# Tenta gerar o próximo subciclo, caso não consiga fechar a sequência não é um ciclo euleriano e retorna False
def get_next_sub_cycle(grafo, visited_edges, current_node):
    sub_cycle = [current_node]
    is_eu_cycle = True
    while True:
        vizinhos = grafo.vizinhos(1 + grafo.nodes.index(current_node))

        # Visita o próximo nó do subciclo
        for node in vizinhos:
            if node not in visited_edges[current_node]:
                next_node = node
                break      
            
        # Se não tiver um próximo nó no subciclo, verifica se o subciclo foi fechado
        # Se sim, para a sequência e retorna, se não, não é um ciclo euleriano.
        if current_node == next_node:
            if sub_cycle[0] == sub_cycle[-1]:
                break
            is_eu_cycle = False
            break
            
        # Atualiza os nós visitados e continua a busca do ciclo.
        sub_cycle.append(next_node)
        visited_edges[current_node] += [next_node]
        visited_edges[next_node] += [current_node]
        current_node = next_node

    return sub_cycle, is_eu_cycle

# file = "../instancias/ciclo_euleriano/SemCicloEuleriano.net"
file = "../instancias/ciclo_euleriano/ContemCicloEuleriano.net"
resultado = ciclo_euleriano(file)
print(resultado)
