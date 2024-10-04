# pylint: disable=all
from avaliacao import Avaliacao
from cardapio.item_cardapio import Itemcardapio

class Restaurante:
    restaurantes=[]
    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.upper()
        self._ativo=False
        self._avaliacao=[]
        self._cardapio=[]
        Restaurante.restaurantes.append(self)
        
    #método especial para mostrar em formato de texto
    #self é a referencia atual da instancia do objeto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
        
    def alternar_estado(self):
       self._ativo=not self._ativo
        
        
    #cls é uma convenção,para indicar que se trata de um método da classe
    @classmethod 
    def listar_restaurantes(cls):
        print(f'{"nome do restaurante".ljust(25)} | {"categoria".ljust(25)} | {"avaliação".ljust(25)} | {"status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo} ')
    #pega o atributo e modifica como ele vai ser lido
    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else "falso"
    
    def receber_avaliacao(self,cliente,nota):
        if(0<nota<=5):
            avaliacao=Avaliacao(cliente,nota)
            self._avaliacao.append(avaliacao)
       
    @property    
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        
        soma_das_notas=sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas=len(self._avaliacao)
        media=round(soma_das_notas/quantidade_notas,1)
        return media
    
    
    def adicionar_cardapio(self,item):
        if isinstance(item,Itemcardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f"cardapio do restaurante: {self._nome}\n")
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,"descricao"):
                mensagem_prato=f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida=f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)
            
        
        
    
    
        
        
if __name__ == "__main__":
    restaurante1 = Restaurante("esquininha", "churrascaria")
    restaurante2 = Restaurante("pizzahut", "pizzaria")
    restaurante3 = Restaurante("dominos", "hamburgueria")

    Restaurante.listar_restaurantes()
    restaurante1.alternar_estado()
    
    print(vars(restaurante1))
    print(restaurante2)
    print(f"o nome do restaurante é {restaurante1._nome}, e é uma {restaurante1._categoria}")