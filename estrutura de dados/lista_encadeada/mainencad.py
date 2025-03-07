from lista_encad import ListaEncadeada

lista=ListaEncadeada()


lista.inserir_final(3)
lista.inserir_inicio(2)
lista.inserir_inicio(1)
lista.inserir_final(4)
lista.inserir_final(5)


print(lista) 


no_encontrado = lista.buscar(3)
print(no_encontrado) 


lista.remover(3)
print(lista)  