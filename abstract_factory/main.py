from factories import *

def initiate_character(factory: CharacterFactory):
    character = factory.create_character()
    weapon = factory.create_weapon()
    armor = factory.create_armor()

    character.introduction()
    weapon.use()
    armor.defend()
    print()

initiate_character(WarriorFactory())
initiate_character(MageFactory())