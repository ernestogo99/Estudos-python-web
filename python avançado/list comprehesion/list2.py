novalista=[numero for numero in range(10) if numero%2==0]
print(novalista)


#lista de quadrados
quadrados=[x**2 for x in range(10)]
print(quadrados)

#números pares de 1 a 20
pares=[x for x in range(1,21) if x%2==0]
print(pares)

#lista com palavras que possuem mais de 5 letras
palavras = ["banana", "uva", "morango", "abacaxi", "kiwi"]
letras5=[palavra for palavra in palavras if len(palavra)>5]
print(letras5)

#números impares de 1 a 20
impares=[x for x in range(1,21) if x%2!=0]
print(impares)

nomes = ["Ana", "Pedro", "Amanda", "João", "Alice"]
nomes_com_a=[nome for nome in nomes if nome.startswith('A')]
print(nomes_com_a)

lista_quadrados=[(x,x**2) for x in range(1,6)]
print(lista_quadrados)


animais = ["cachorro", "gato", "elefante", "gato"]
nova_lista_animais=['Leão' if animal=='gato' else animal for animal in animais ]
print(nova_lista_animais)

#matriz 3x3
matriz=[[j for j in range(1,4)]for i in range(3)]
print(matriz)