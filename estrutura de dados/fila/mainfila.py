from filalista import Fila
from filaencad import FilaEncad
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(fila.primeiro_fila())  
print(fila.desenfileirar())  
print(fila.tamanho())  


fila = FilaEncad()
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
print(fila) 
print(fila.primeiro_fila())  
print(fila.ultimo_fila())    
print(fila.desinfileirar()) 
print(fila)  
print(fila.tam())  