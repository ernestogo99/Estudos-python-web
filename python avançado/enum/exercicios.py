from enum import Enum,Flag,auto


#dias da semana

class Semana(Enum):
    MONDAY:int=1
    TUESDAY:int=2
    WEDNESDAY:int=3
    THURSDAY:int=4
    FRIDAY:int=5
    SATURDAY:int=6
    SUNDAY:int=7
    
print(Semana.MONDAY.name)
print(Semana.MONDAY.value)

class Permissions(Flag):
    READ=auto()
    WRITE=auto()
    EXECUTE=auto()
    DELETE=auto()
    
    
combined_permission:Permissions=Permissions.READ | Permissions.WRITE
user_permission:Permissions=Permissions.WRITE
print(combined_permission)
print(user_permission in combined_permission)