# pylint: disable=all
#numpy=numerical python
import numpy as np

lista=np.array([3,16,9,28])#array ou ndarray
print(lista)

lista0=np.zeros(10)

print(lista0)

lista1=np.ones(3)
print(lista1)

lista20=np.empty(20)

lista1_9=np.arange(1,10,3)
print(lista1_9)


L=[3,16,9,28,99,16,54,21,7]

arr=np.array(L)
arr.sort()
print(arr)

x=np.array([6,5,4])
novo_array=np.concatenate((x,arr))
print(novo_array)
x.shape # mostra a forma
x.ndim # mostra a dimensão 
print(x.size)