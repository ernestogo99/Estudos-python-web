# pylint: disable=all
from cardapio.item_cardapio import  Itemcardapio


#herança em python basta passar o itemcardapio(classe) como parametro
class Prato(Itemcardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self.descricao=descricao
        
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -=(self._preco *0.08)