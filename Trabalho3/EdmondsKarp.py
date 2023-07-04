from Grafo import Grafo


def main(file):
    grafo = Grafo(file)
    grafoResidual = Grafo(file)
    fluxo_max = edmondsKarp(grafo, grafoResidual)
    print(fluxo_max)
    
def edmondsKarp(G, GR):
    grafo = G
    grafoResidual = GR
    s = 1
    t = grafo.nodes.index(grafo.nodes[-1])+1
    
    #Zera as arestas
    for node in grafo.nodes:
        node = grafo.nodes.index(node) + 1
        vizinhos = grafo.getVizinhosIndex(node)
        for vizinho in vizinhos:
            grafoResidual.delAresta(node, vizinho)
            grafoResidual.setPeso(node, vizinho, 0)
            grafoResidual.setPeso(vizinho, node, 0)
        
    caminho = caminhoAumentante(grafo, grafoResidual, s, t)
    
    while caminho != None:
        fluxo = min(grafo.getPeso(u, v) - grafoResidual.getPeso(u, v) for u,v in caminho)
        for u,v in caminho:
            grafoResidual.addPeso(u, v, fluxo)
            grafoResidual.addPeso(v, u, -fluxo)
        caminho = caminhoAumentante(grafo, grafoResidual, s, t)
    
    sVizinhos = grafoResidual.getVizinhosIndex(s)
    fluxo_max = sum(grafoResidual.getPeso(s, vizinho) for vizinho in sVizinhos)
    return fluxo_max
        
        
        
#BFS
def caminhoAumentante(grafo, grafoResidual, s, t):
        fila = [s]
        caminho = {s:[]}
        if s == t:
            return caminho[s]
        
        while fila: 
            u = fila.pop(0)
            for v in range(grafo.getQtdVertices()):
                v+=1
                pesoG = grafo.getPeso(u, v)
                pesoGR = grafoResidual.getPeso(u, v) 
                
                if (pesoG - pesoGR > 0) and v not in caminho:
                    caminho[v] = caminho[u]+[(u,v)]
                    if v == t:
                        return caminho[v]
                    fila.append(v)
                    
        return None


file = "../instancias/fluxo_maximo/fluxo.net"
main(file)