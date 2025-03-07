class Noh:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
        
    def __repr__(self):
        return f'NOH {self.dado}'
    
    
class PilhaEncad:
    def __init__(self):
        self.topo=None
        self.tam=0
        
    def __repr__(self):
        nos=[]
        atual=self.topo
        while atual:
            nos.append(repr(atual))
            atual=atual.proximo   
        return ' -> '.join(nos)
    
    def inserir_topo(self, dado):
        novo_noh = Noh(dado)
        novo_noh.proximo = self.topo
        self.topo = novo_noh
        self.tam += 1

        
    def top(self):
        if self.vazia():
            return 'pilha vazia'
        return self.topo.dado
    
    def vazia(self):
        return self.topo==None
    
    def remover_topo(self):
        if self.vazia():
            return 'pilha vazia'
        elemento=self.topo.dado
        self.topo=self.topo.proximo
        self.tam-=1
        return elemento
    
    def tamanho(self):
        return self.tam
        