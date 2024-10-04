usuarios_data_science=[15,23,45,68]

usuarios_machine_learning=[13,23,56,42]

assistiram=[]
assistiram.extend(usuarios_data_science)#esse método percorre o vetor e adiciona os elementos a outro
print(f"assistiram: {assistiram}")

assistiram=usuarios_machine_learning.copy()
print(f"copia: {assistiram}")

assistiram.extend(usuarios_data_science)
assistiram.append(22)
print(f"o tamanho é :{len(assistiram)}")

conjunto=set(assistiram)
print(f"o tamanho do conjunto: {conjunto} é {len(conjunto)}")

for usuario in conjunto:
    print(f"usuario: {usuario}")
    


conjunto2={45,2,3,1}

#união dos conjuntos(|)

uniao=conjunto | conjunto2

print(f"a uniao dos conjuntos é {uniao}")

#interseção dos conjuntos(&)

intersecao=conjunto & conjunto2
print(f"a intersecao dos conjuntos é {intersecao}")

#quem está no conjunto1 e não está no 2:
menos=conjunto-conjunto2
print(f"menos: {menos}")

usuarios={1,5,76,34,52,13,17}
usuarios.add(29)

print(usuarios)

usuarios_congelados=frozenset(usuarios)
#não é possivel adicionar elementos em um conjunto congelado, conjunto imutavel
