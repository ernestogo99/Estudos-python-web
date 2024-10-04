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

