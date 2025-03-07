from arvorebin import Arvore
arvore = Arvore()


valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arvore.inserir(valor)


print(arvore)

arvore.imp()

no_encontrado = arvore.buscar(40)
print(no_encontrado) 


