class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
 
    def is_alive(self):
        return self.hp > 0

class Guard(Enemy):
    def __init__(self):
        super().__init__(name="Guard", hp=10, damage=2)
 
class Ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre", hp=30, damage=15)

class Dog(Enemy):
    def __init__(self):
        super().__init__(name="Dog", hp=20, damage=10)

class Miller(Enemy):
    def __int__(self):
        super().__init__(name="Miller", hp=50, damage=10)

class Leon(Enemy):
    def __int__(self):
        super().__init__(name="Leon", hp=50, damage=10)
