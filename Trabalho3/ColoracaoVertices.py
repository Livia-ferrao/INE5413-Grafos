from Grafo import Grafo

def main(file):
    grafo = Grafo(file)
    nodes = sorted(grafo.nodes, key=lambda node: len(grafo.getVizinhos(int(node))), reverse=True)
    colors = []

    for node in nodes:
        colors_aux = [True] * len(nodes)
        for vizinho in grafo.getVizinhos(int(node)):
            if grafo.cor[int(vizinho)-1] != None:
                colors_aux[grafo.cor[int(vizinho)-1]] = False

        for cor, available in enumerate(colors_aux):
            if available:
                grafo.cor[int(node)-1] = cor
                if cor not in colors:
                    colors.append(cor)
                break

    print("Coloração mínima:", len(set(grafo.cor)))
    for index, node in enumerate(grafo.nodes):
        print(f'{index+1} : {grafo.cor[int(node)-1]}')

main("../instancias/coloracao/cor3.net")