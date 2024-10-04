# pylint: disable=all
from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo,qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas=qtd_portas
    
    def __str__(self):
     status = "ligado" if self._ligado else "desligado"
     return f"{self.marca} {self.modelo} - Portas: {self.qtd_portas} - Status: {status}"
    