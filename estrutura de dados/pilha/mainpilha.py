from  pilhalista import Pilha
from pilhaencad import PilhaEncad
import time

start=time.time()
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)
print(pilha.topo())  
print(pilha.desempilhar()) 
print(pilha.tamanho())
end=time.time() 
print(f"Pilha com vetor: {end - start:.5f} segundos")

start=time.time()
pilha_encad=PilhaEncad()
pilha_encad.inserir_topo(1)
pilha_encad.inserir_topo(2)
pilha_encad.inserir_topo(3)
print(pilha_encad.top())
print(pilha_encad.remover_topo())
print(pilha_encad.tamanho())
end=time.time()
print(f"Pilha com lista encadeada: {end - start:.5f} segundos")