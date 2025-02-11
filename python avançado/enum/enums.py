from enum import Enum,Flag,auto
#O módulo enum do Python permite criar enumeradores,
# que são conjuntos de valores nomeados e imutáveis. 
# Ele é útil para representar estados, cores, tipos, opções, entre outros, 
# tornando o código mais organizado e legível.

class Combination(Flag):
    RED:int =auto()
    GREEN:int =auto()
    BLUE:int =auto()
    YELLOW:int=auto()
    BLACK:int =auto()
    ALL: RED | GREEN | BLACK | YELLOW | BLUE

class State(Enum):
    OFF:int =0
    ON:int = 1

class Color(Enum):
    RED:str = 'R'
    GREEN:str = 'G'
    BLUE:str = 'B'

class ColorFlag(Flag):
    RED:int =1
    GREEN:int =2
    BLUE:int =4
    YELLOW:int=8
    BLACK:int =16    

yellow_and_red:ColorFlag=ColorFlag.YELLOW | ColorFlag.RED
print(yellow_and_red)
for color in yellow_and_red:
    print(color)

cool_colors:ColorFlag=ColorFlag.RED | ColorFlag.BLACK | ColorFlag.YELLOW
my_car_color=ColorFlag.BLACK

if my_car_color in cool_colors:
    print('carro legal')
else:
    print("não é legal")
    
print(Color('R'))
print(repr(Color.RED))
print(Color.RED.name)
print(Color.RED.value)

def create_car(color:Color):
    match color:
        case Color.RED:
            print(f'um carro vermelho foi criado')
        
        case Color.BLUE:
            print(f'um carro azul foi criado')
        
        case Color.GREEN:
            print(f'um carro verde foi criado')
        
        case _:
            print(f'não temos a cor ${color} no banco de dados')
            
create_car(Color.GREEN)

switch:State = State.ON

match switch:
    case State.ON:
        print('a lâmpada está ligada')
    case State.OFF:
        print("a lâmpada está desligada")
    case _:
        print("nada")