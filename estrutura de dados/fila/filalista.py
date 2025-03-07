class Fila:
    def __init__(self):
        self.items=[]
        
    def enfileirar(self,item):
        self.items.append(item)
        
    def vazia(self):
        return len(self.items)==0
    
    def primeiro_fila(self):
        return self.items[0]
    
    def ultimo_fila(self):
        return self.items[0]
    
    def tamanho(self):
        return len(self.items)    
    
    def desenfileirar(self):
        if self.vazia():
            return
        return self.items.pop(0)