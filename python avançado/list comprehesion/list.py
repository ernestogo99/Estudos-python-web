#List comprehesion
#uma sintaxe mais curta para criar uma lista baseada em uma lista já existente
#Sintaxe: novalista=[expressão for item in interable if condition==True]

animais=['cachorro','gato','tartaruga','girafa']
nova_lista=[]

for animal in animais:
    if 't' in animal:
        nova_lista.append(animal)
        
print(nova_lista)



#usando list_comprehesion
list=[animal for animal in animais if 't' in animal]
print(f' a nova lista é {list}')

animais_upper=[animal.upper() for animal in animais ]
print(animais_upper)


novos_animais=[animal if animal!='cachorro' else 'macaco' for animal in animais]
print(novos_animais)