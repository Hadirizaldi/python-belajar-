class Hero :
    jumlah_hero = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor) :
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    def siapa(self):
        print(f"namaku adalah {self.name}")
    
    def healthUp(self,up) :
        self.health = self.health + up

    def getHealth(self) :
        return self.health

hero1 = Hero('sniper', 100,10,5)
hero2 = Hero('Miya', 200,25,4)

print(hero1.__dict__)
print(hero2.__dict__)

hero1.siapa()
hero1.healthUp(30)

print(f'\nAttribute : \n{hero1.__dict__}')
print(f'\nhealth :\n{hero1.getHealth()}')