from elements import *

class CharacterFactory(ABC):
    @abstractmethod
    def create_character(self) -> Character:
        pass

    @abstractmethod
    def create_weapon(self) -> Weapon:
        pass

    @abstractmethod
    def create_armor(self) -> Armor:
        pass


class WarriorFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Warrior()

    def create_weapon(self) -> Weapon:
        return Sword()

    def create_armor(self) -> Armor:
        return Shield()


class MageFactory(CharacterFactory):
    def create_character(self) -> Character:
        return Mage()

    def create_weapon(self) -> Weapon:
        return Staff()

    def create_armor(self) -> Armor:
        return Robe()
