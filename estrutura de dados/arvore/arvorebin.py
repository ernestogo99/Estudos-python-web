class Noh:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

    def __repr__(self):
        return f'No({self.dado})'


class Arvore:
    def __init__(self):
        self.raiz = None

    def __repr__(self):
        return self._repr_aux(self.raiz, 0)

    def _repr_aux(self, no:Noh, nivel):
        if no is None:
            return ""
        espacos = " " * (nivel * 4)
        resultado = f"{espacos}{no.dado}\n"
        resultado += self._repr_aux(no.esq, nivel + 1)
        resultado += self._repr_aux(no.dir, nivel + 1)
        return resultado

    def imprimir(self,no:Noh):
        if no:
            self.imprimir(no.esq)
            print(f'Noh {no.dado} ')
            self.imprimir(no.dir)
            
    def imp(self):
        self.imprimir(self.raiz)

    def _inserir_rec(self, no:Noh, dado):
        if no is None:
            return Noh(dado)
        if dado < no.dado:
            no.esq = self._inserir_rec(no.esq, dado)
        elif dado > no.dado:
            no.dir = self._inserir_rec(no.dir, dado)
        return no

    def inserir(self, valor):
        self.raiz = self._inserir_rec(self.raiz, valor)

    
    def _buscar_rec(self,no:Noh,valor):
        if no is None or no.dado==valor:
            return no
        if valor < no.dado:
            return self._buscar_rec(no.esq,valor)
        return self._buscar_rec(no.dir,valor)    
    
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)   
    
    def _tamanho(self,noh:Noh):
        if noh is None:
            return 0
        return 1+self._tamanho(noh.esq) + self._tamanho(noh.dir)
    
    def tam(self):
        return self._tamanho(self.raiz) 