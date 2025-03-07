class Noh:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
        
    def __repr__(self):
        return f'Noh {self.dado}'
    
    
class FilaEncad:
    def __init__(self):
        self.inicio=None
        self.fim=None
        self.tamanho=0
        
    def __repr__(self):
        nos=[]
        atual=self.inicio
        while atual:
            nos.append(repr(atual))
            atual=atual.proximo   
        return ' -> '.join(nos)
    
    def enfileirar(self, dado):
        novo_noh = Noh(dado)
        if not self.fim:
            self.inicio = novo_noh
            self.fim = novo_noh
        else:
            self.fim.proximo = novo_noh
            self.fim = novo_noh
        self.tamanho += 1
        
    def vazia(self):
        return self.fim==None 
    
    def primeiro_fila(self):
        if self.vazia():
            return 'Fila vazia'
        return self.inicio.dado
    
    def ultimo_fila(self):
        if self.vazia():
            return 'Fila vazia'
        return self.fim.dado
    
    def tam(self):
        return self.tamanho
    
    def desinfileirar(self):
        if self.vazia():
            return 'fila vazia'
        
        elemento=self.inicio.dado
        self.inicio=self.inicio.proximo
        self.tamanho-=1
        if self.inicio==None:
            self.fim=None
        return elemento
            