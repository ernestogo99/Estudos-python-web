# uma função lambda é uma pequena função anônima
#recebe os argumentos porém só pode executar uma expressão
#lambda argumentos: expressão
#Elas são úteis para funções curtas e rápidas, especialmente quando usadas como argumentos em funções como map(), filter() e sorted().
x=lambda a:a*3
print(x(4))

soma= lambda a,b:a+b
print(soma(5,8))

graus_celcius=lambda f:(5/9)*(f-32)
print(f'a temperatura em graus celsius é {graus_celcius(32)}')

#Dobrar os números de uma lista
lista =[1,2,3,4,5]
#map(função,iteravel)
dobrados=list(map(lambda x:x*2,lista))
print(dobrados)

#filtrar numeros pares
lista2=[6,7,8,9,10]
pares=list(filter(lambda x:x%2==0,lista2))
print(pares)

#ordenar uma lista de tuplas pelo segundo elemento
pessoas = [("Ana", 25), ("Bruno", 30), ("Carlos", 22)]
ordenado_por_idade=sorted(pessoas,key=lambda x:x[1])
print(ordenado_por_idade)