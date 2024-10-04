class Grafo:
    def __init__(self):
        self.vertices={}
        
    
    def add_vertice(self,nome):
        if nome not in self.vertices:
            self.vertices[nome]=[]
            
    
    def inserir_aresta(self,origem,destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            
            
    def remover_aresta(self,origem,destino):
        if origem in self.vertices and destino in self.vertices[origem]:
            self.vertices[origem].remove(destino)
            
    def imprimir_grafo(self):
        for vertice,vizinhos in self.vertices.items():
            print(f"Vértice: {vertice}: ",end="")
            for vizinho in vizinhos:
                print(f"-> {vizinho}: ",end="")
            print()
            
    def buscar_vertice(self,nome):
       return nome in self.vertices
   
g = Grafo()

g.add_vertice("A")
g.add_vertice("B")
g.add_vertice("C")

g.inserir_aresta("A", "B")
g.inserir_aresta("B", "C")
g.inserir_aresta("C", "A")

print(g.buscar_vertice("A"))
g.imprimir_grafo()

        
        