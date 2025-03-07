class Pilha:
    def __init__(self):
        self.items=[]
        
    def empilhar(self,item):
        self.items.append(item)
        
    def vazia(self):
        return len(self.items)==0
    
    def desempilhar(self):
        if self.vazia():
            return
        return self.items.pop()
        
    def topo(self):
        if self.vazia():
            return
        return self.items[-1]
    
    def tamanho(self):
        return len(self.items)
    
        
        