from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def introduction(self):
        pass

class Weapon(ABC):
    @abstractmethod
    def use(self):
        pass

class Armor(ABC):
    @abstractmethod
    def defend(self):
        pass


# Warrior Implementation
class Warrior(Character):
    def introduction(self):
        print("I am a warrior! Now you shall meet the wrath of my blade!")

class Sword(Weapon):
    def use(self):
        print("Swinging the sword!")

class Shield(Armor):
    def defend(self):
        print("Blocking with a shield")


# Mage Implementation
class Mage(Character):
    def introduction(self):
        print("Magic can hurt, respect that!")

class Staff(Weapon):
    def use(self):
        print("Casting spells with staff!")

class Robe(Armor):
    def defend(self):
        print("Magic robe absorbs damage")
