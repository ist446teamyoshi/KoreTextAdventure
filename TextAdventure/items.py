# Base class for all items
class Item():
    # __init__ is the contructor method
    def __init__(self, name, description, value):
        self.name = name   # attribute of the Item class and any subclasses
        self.description = description # attribute of the Item class and any subclasses
        self.value = value # attribute of the Item class and any subclasses
    
    # __str__ method is used to print the object
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

# Extend the Items class
# Gold class will be a child or subclass of the superclass Item
class Gold(Item):
    # __init__ is the contructor method
    def __init__(self, amt): 
        self.amt = amt # attribute of the Gold class
        super().__init__(name="Gold",
                         description="A round coin with {} stamped on the front.".format(str(self.amt)),
                         value=self.amt)

class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
 
class Laser(Weapon):
    def __init__(self):
        super().__init__(name="Laser",
                         description="A laser gun. Made from Kore technology.",
                         value=50,
                         damage=5)
 
class Whip(Weapon):
    def __init__(self):
        super().__init__(name="Whip",
                         description="A leather whip. Try not to hit yourself with it.",
                         value=10,
                         damage=2)
class Mine(Weapon):
    def __init__(self):
        super().__init__(name="Mine",
                         description="A mine that triggers with motion.",
                         value=20,
                         damage=10)

class Shruiken(Weapon):
    def __init__(self):
        super().__init__(name="Shruiken",
                         description="An authentic japanese shruiken. It looks pretty sharp.",
                         value=20,
                         damage=5)