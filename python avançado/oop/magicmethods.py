import uuid

class Archer:
    
    def __init__(self,hp,mana,arrows):
        self.hp=hp
        self.mana=mana
        self.arrows=arrows
        self._id=uuid.uuid4()
    
    def __str__(self):
        return f'{self.hp}-hp | {self.mana}-mana | {self.arrows}-arrows'
    
    def __repr__(self):
        return  f'Archer({self.hp}, {self.mana}, {self.arrows})'
    
    def __add__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        new_hp=self.hp+other.hp
        new_mana=self.mana + other.mana
        new_arrows=self.arrows + other.arrows
        return Archer(new_hp,new_mana,new_arrows)
    
    def __eq__(self, other):
        if not isinstance(other,Archer):
            return False
        return self.hp==other.hp and self.mana==other.mana and self.arrows==other.arrows
    
    def __gt__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        return self.hp > other.hp
    
    def __lt__(self,other):
        if not isinstance(other,Archer):
            return NotImplemented
        return self.hp < other.hp
    
    def __hash__(self):
        return hash(self._id)
    
archer1=Archer(100,100,5)
archer2=Archer(100,100,5)
print(archer1)
archer3=archer1+archer2
print(archer3)
print(archer1==archer2)

new_dict={archer1:'test'}

class Company:
    def __init__(self,size):
        self.size=size
        self.archers=[]
        self.index=0
        
    def add_acher(self,archer):
        if not isinstance(archer,Archer):
            raise TypeError("Only arches allowed")
        if len(self.archers)>self.size:
            raise ValueError ("Company already full")
        self.archers.append(archer)
     
    def __add__(self,other):
        if not isinstance(other,Archer):
            raise TypeError("Only arches allowed")
        self.add_acher(other)
        return self  
    
    def list_archers(self):
        for archer in self.archers:
            print(archer)
            
    def __iter__(self):
        return iter(self.archers)
    
    
    def __next__(self):
        if self.index >=len(self.archers):
            raise StopIteration
        archer=self.archers[self.index]
        self.index+=1
        return archer
        
company=Company(5)
company.add_acher(archer2)
new_company=company+archer1
print(company.archers)
print(new_company.archers)
new_company.list_archers()
for archer in new_company.archers:
    print(f'arqueiro: {archer}')