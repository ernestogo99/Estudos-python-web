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