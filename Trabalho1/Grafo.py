import numpy as np

class Grafo:
    def __init__(self, filename=False):
        self.graph = dict() #cria a lista de adjacencia (dicionario)
        self.nodes = []  #guardar nos
        self.edges = 0 #guardar numero de arestas
        self.dim = 0 #guardar numero de vertices

        with open(filename) as f:
            self.dim = int(f.readline().split()[1]) #guardar numero de vertices
            self.matrix = np.full((self.dim, self.dim), np.inf) #matriz de infinitos
            for line in f: #adicionar key(rotulo) ao dicionario ate encontrar a linha *edges
                dirigido = False
                if "*edges" in line:
                    break
                if "*arcs" in line:
                    dirigido = True
                    break
                
                #spilt line no numero e no rotulo
                parts = line.split(' ', 1)
                num = int(parts[0])
                name = parts[1].rstrip('\n').strip('"')

                self.nodes += [name] #guardar rotulos
                self.graph[name]= []

                self.matrix[num-1][num-1] = 0 #pesos entre um no e ele mesmo é zero
            
            if len(self.nodes) == 0:
                for i in range(0, self.dim):
                    self.nodes += [i] #guardar rotulos
                    self.graph[i]= []

            if not dirigido:
                for line in f:
                    node1 = int(line.split()[0])
                    node2 = int(line.split()[1])
                    weight = float(line.split()[2])
                    
                    #Faz lista adjacencia
                    self.graph[self.nodes[node1-1]] += [(self.nodes[node2-1], weight)] #adiciona aresta e lista de adjacencia 
                    self.graph[self.nodes[node2-1]] += [(self.nodes[node1-1], weight)]

                    #Faz matriz de adjacencia
                    self.matrix[node1-1][node2-1] = weight
                    self.matrix[node2-1][node1-1] = weight 

                    self.edges +=1
            else:
                for line in f:
                    node1 = int(line.split()[0])
                    node2 = int(line.split()[1])
                    weight = float(line.split()[2])

                    #Faz lista adjacencia
                    self.graph[self.nodes[node1-1]] += [(self.nodes[node2-1], weight)]

                    #Faz matriz de adjacencia
                    self.matrix[node1-1][node2-1] = weight

    def qtdVertices(self):
        return self.dim
    
    def qtdArestas(self):
        return self.edges
    
    def grau(self, v):
        if v >= 1 and v <= self.dim:
            return len(self.graph[self.nodes[v-1]])
        else:
            raise AssertionError("Error: node out of scope")
    
    #Recebe o valor do vértice, retorna o vértice
    def rotulo(self, v):
        if v >= 1 and v <= self.dim:
            return self.nodes[v-1]
        else:
            raise AssertionError("Error: node out of scope")
        
    #Recebe o valor do vértice, retorna os  seus vizinhos
    def vizinhos(self, v): 
        if v >= 1 and v <= self.dim:
            neighbors=[]
            for i in range (len(self.graph[self.nodes[v-1]])):
                neighbors += [self.graph[self.nodes[v-1]][i][0]] 
            return neighbors
        else:
            raise AssertionError("Error: node out of scope")

    def vizinhos_index(self,v):
        viz = self.vizinhos(v)
        neighbors_index = []
        for i in range(len(viz)):
            neighbors_index += [self.nodes.index(viz[i])+1]
        return neighbors_index

    #Recebe valor dois vértices, retorna se estão conectados (Caso não esteja declarado, retorna inf)
    def haAresta(self, u, v): 
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.rotulo(v):
                    return True
            return float('inf')
        else:
            raise AssertionError("Error: node out of scope")
    
    #Recebe valor de dois vértices, retorna o peso entre eles (Caso não esteja declarado, retorna inf)
    def peso(self, u, v):
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.rotulo(v):
                    return self.graph[self.nodes[u-1]][i][1]
            return float('inf')
        else:
            raise AssertionError("Error: node out of scope")
    
    def matrizAdj(self):
        return self.matrix
    
    def getTransposedGraph(self):
        listaAdjacencias = dict()

        # Inicializa
        for key in self.graph.keys():
            listaAdjacencias.setdefault(key, [])

        # Insere arcos invertendo a direção. Se a = (v, u), a' = (u, v)
        for i, vertice in self.graph.items():
            for _ , aresta in enumerate(vertice):
                listaAdjacencias[aresta[0]].append((i, aresta[1]))

        self.graph = listaAdjacencias
        return self.graph 

