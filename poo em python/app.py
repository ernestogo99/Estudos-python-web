# pylint: disable=all
from restaurante import Restaurante
from cardapio.bebida import Bebida
from cardapio.prato import Prato


Restaurante.restaurantes=[]

restaurante_praca = Restaurante("praca", "gourmet")
bebida_suco=Bebida('suco de melancia',5,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho=Prato('paozinho',2,'o melhor')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_cardapio(bebida_suco)
restaurante_praca.adicionar_cardapio(prato_paozinho)


def main():
    restaurante_praca.exibir_cardapio

if __name__ == "__main__":
    main()
