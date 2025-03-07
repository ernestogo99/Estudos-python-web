class Archer:
    def __init__(self,hp,dmg):
        self._hp=hp
        self._dmg=dmg
        self.crit=1.3
        self._overall_damage= None
        
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def set_hp(self,value):
        if value >200:
            raise ValueError ("HP can be 200 at max")
        self._hp=value
        
    @property
    def dmg(self):
        return self._dmg
    
    @dmg.setter
    def dmg(self,value):
        self._overall_damage=None
        self._dmg=value
        
    @property
    def overall_damage(self):
        self._overall_damage= self.dmg * self.crit
        return self._overall_damage
    

    @overall_damage.setter
    def overall_damage(self,value):
        raise ValueError("Changing overall damage not allowed")
    
archer1=Archer(100,20)
archer1.dmg=35
print(archer1.overall_damage)