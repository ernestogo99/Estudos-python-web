from abc import ABC,abstractmethod

class Itemcardapio(ABC):
    def __init__(self,nome,preco):
        self._nome=nome
        self._preco=preco
        
    #todas as classes derivadas precisam ter esse método implementado
    @abstractmethod
    def aplicar_desconto(self):
        pass
        