class Noh:
    def __init__(self,dado):
        self.dado=dado
        self.proximo=None
    
    def __repr__(self):
        return f'Noh {self.dado}'


class ListaEncadeada:
    def __init__(self):
        self.cabeca=None   
        self.final=None
        
    def __repr__(self):
        nos=[]
        atual=self.cabeca
        while atual:
            nos.append(repr(atual))
            atual=atual.proximo   
        return ' -> '.join(nos) 
    
    def inserir_inicio(self,dado):
        novo_noh=Noh(dado)
        if not self.cabeca:
            self.cabeca=novo_noh
            self.final=novo_noh
            return
        novo_noh.proximo=self.cabeca
        self.cabeca=novo_noh 
        
    def inserir_final(self,dado):
        novo_noh=Noh(dado)
        if not self.final:
            self.cabeca=novo_noh
            self.final=novo_noh
            return
        self.final.proximo=novo_noh
        self.final=novo_noh
        
    def buscar(self,dado):
        atual=self.cabeca
        while atual and atual.dado!=dado:
            atual=atual.proximo
        return atual
    
    def remover(self,dado):
        atual=self.cabeca
        anterior=None
        while atual and atual.dado!=dado:
            anterior=atual
            atual=atual.proximo
        if not atual:
            return
        if not anterior:
            self.cabeca=atual.proximo
        else:
            anterior.proximo=atual.proximo
        atual.proximo=None
            
            