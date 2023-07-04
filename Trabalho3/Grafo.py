import numpy as np

class Grafo:
    def __init__(self, filename=False):
        self.graph = dict() #cria a lista de adjacencia (dicionario)
        self.nodes = []  #guardar nos
        self.edges = 0 #guardar numero de arestas
        self.dim = 0 #guardar numero de vertices
        self.cor = None #para coloração de grafos

        with open(filename) as f:
            self.dim = int(f.readline().split()[1]) #guardar numero de vertices
            self.cor = [None] * self.dim # array de cores
            self.matrix = np.full((self.dim, self.dim), np.inf) #matriz de infinitos
            dirigido = False
            for line in f: #adicionar key(getRotulo) ao dicionario ate encontrar a linha *edges
                # print(line)
                if "*edges" in line:
                    break
                if "*arcs" in line:
                    dirigido = True
                    break
                
                #spilt line no numero e no getRotulo
                parts = line.split(' ', 1)
                num = int(parts[0])
                name = parts[1].rstrip('\n').strip('"')

                # num = int(line.split()[0])
                # name = line[line.find('"')+1:-2]

                self.nodes += [name] #guardar getRotulos
                self.graph[name]= []

                self.matrix[num-1][num-1] = 0 #pesos entre um no e ele mesmo é zero
            
            if len(self.nodes) == 0:
                for i in range(0, self.dim):
                    self.nodes += [i] #guardar getRotulos
                    self.graph[i]= []

            if not dirigido:
                for line in f:
                    node1 = int(line.split()[0])
                    node2 = int(line.split()[1])
                    weight = float(line.split()[2])
                    
                    #Faz lista adjacencia
                    self.graph[self.nodes[node1-1]] += [[self.nodes[node2-1], weight]] #adiciona aresta e lista de adjacencia 
                    self.graph[self.nodes[node2-1]] += [[self.nodes[node1-1], weight]]

                    #Faz matriz de adjacencia
                    self.matrix[node1-1][node2-1] = weight
                    self.matrix[node2-1][node1-1] = weight 

                    self.edges +=1
                    
                    self.X = set()  # First partition
                    self.Y = set()  # Second partition

                    # Perform BFS traversal to assign nodes to partitions
                    visited = set()
                    queue = []
                    for node in self.nodes:
                        if node not in visited:
                            queue.append(node)
                            self.X.add(node)  # Add the first node to partition X
                            visited.add(node)

                            while queue:
                                current_node = queue.pop(0)
                                neighbors = self.graph[current_node]
                                for neighbor in neighbors:
                                    if neighbor[0] not in visited:
                                        if current_node in self.X:
                                            self.Y.add(neighbor[0])  # Assign neighbor to partition Y
                                        else:
                                            self.X.add(neighbor[0])  # Assign neighbor to partition X
                                        visited.add(neighbor[0])
                                        queue.append(neighbor[0])
                                        
            else:
                for line in f:
                    node1 = int(line.split()[0])
                    node2 = int(line.split()[1])
                    weight = float(line.split()[2])

                    #Faz lista adjacencia
                    self.graph[self.nodes[node1-1]] += [[self.nodes[node2-1], weight]]

                    #Faz matriz de adjacencia
                    self.matrix[node1-1][node2-1] = weight

    def getQtdVertices(self):
        return self.dim
    
    def getQtdArestas(self):
        return self.edges
    
    def getGrau(self, v):
        if v >= 1 and v <= self.dim:
            return len(self.graph[self.nodes[v-1]])
        else:
            raise AssertionError("Error: node out of scope")
    
    #Recebe o valor do vértice, retorna o vértice
    def getRotulo(self, v):
        if v >= 1 and v <= self.dim:
            return self.nodes[v-1]
        else:
            raise AssertionError("Error: node out of scope")
        
    #Recebe o valor do vértice, retorna os  seus vizinhos
    def getVizinhos(self, v): 
        if v >= 1 and v <= self.dim:
            neighbors=[]
            for i in range (len(self.graph[self.nodes[v-1]])):
                neighbors += [self.graph[self.nodes[v-1]][i][0]] 
            return neighbors
        else:
            raise AssertionError("Error: node out of scope")
        
    def getIndex(self, v):
        return self.nodes.index(v)+1
    
    def getVizinhosIndex(self,v):
        viz = self.getVizinhos(v)
        neighbors_index = []
        for i in range(len(viz)):
            neighbors_index += [self.nodes.index(viz[i])+1]
        return neighbors_index

    #Recebe valor dois vértices, retorna se estão conectados (Caso não esteja declarado, retorna inf)
    def getHaAresta(self, u, v): 
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.getRotulo(v):
                    return True
            return float('inf')
        else:
            raise AssertionError("Error: node out of scope")
    
    def delAresta(self, u, v):
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.getRotulo(v):
                    self.graph[self.getRotulo(u)].pop(i) 
                    break
        else:
            raise AssertionError("Error: node out of scope")
       
    #Recebe valor de dois vértices, retorna o peso entre eles (Caso não esteja declarado, retorna inf)
    def getPeso(self, u, v):
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.getRotulo(v):
                    return self.graph[self.nodes[u-1]][i][1]
            return float('inf')
        else:
            raise AssertionError("Error: node out of scope")
    
    def setPeso(self, u, v, value):
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            self.graph[self.nodes[u-1]] += [[self.nodes[v-1], value]]
        else:
            raise AssertionError("Error: node out of scope")
    
    def addPeso(self, u, v, value):
        if u >= 1 and u <= self.dim and v >= 1 and v <= self.dim:
            for i in range (len(self.graph[self.nodes[u-1]])):
                if self.graph[self.nodes[u-1]][i][0] == self.getRotulo(v):
                    self.graph[self.nodes[u-1]][i][1] += value
        else:
            raise AssertionError("Error: node out of scope")
    
    def getMatrizAdj(self):
        return self.matrix
    
    # Insere arcos invertendo a direção. Se a = (v, u), a' = (u, v)
    def getTransposedGraph(self):
        listaAdjacencias = dict()

        for key in self.graph.keys():
            listaAdjacencias.setdefault(key, [])

        for i, vertice in self.graph.items():
            for _ , aresta in enumerate(vertice):
                listaAdjacencias[aresta[0]].append((i, aresta[1]))

        self.graph = listaAdjacencias
        return self.graph 
    
    # Retorna todas as arestas
    def getEdges(self):
        edges = []
        for key, values in self.graph.items():
            for value in values:
                reverse_edge = (int(value[0])-1, int(key)-1)
                if reverse_edge not in edges:
                    edges.append((int(key)-1, int(value[0])-1))
        return edges
    
    # Retorna todos os vertices
    def getNodes(self):
        nodes = []
        for _, node in enumerate (self.graph.keys()):
            print(node)
            nodes.append(node)
        return nodes
    
