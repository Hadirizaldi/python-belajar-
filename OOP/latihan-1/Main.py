class Hero :
    name = ""
    health = 0
    attackPower = 0
    armorNumber = 0

    def __init__(self,name,health,attackPower,armorNumber) :
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber
    
    def actionAttack(self, enemy) :
        print(f'\n{self.name} attacking {enemy.name}\n')
        enemy.attacked(self, self.attackPower)
    
    def attacked(self, enemy, enemy_attackPower) :
        print(f'{self.name} attacked {enemy.name}')
        attackReceived = enemy_attackPower/self.armorNumber
        print(f'attack damage: {attackReceived} ')
        self.health -= attackReceived
        print(f'health from {self.name} left : {self.health}')
        self.isDeath()

    def isDeath(self) :
        if (self.health <= 0) :
            print(f'{self.name} is defeated')

# init hero
hayabusa = Hero('Hayabusa',100,10005,3)
akai = Hero('Akai',100,5,12)

# action
hayabusa.actionAttack(akai)
