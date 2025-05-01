from factories import *
from time import sleep
import random, threading

def initiate_character(factory: CharacterFactory):
    character = factory.create_character()
    weapon = factory.create_weapon()
    armor = factory.create_armor()

    sleep(random.random()*3)

    character.introduction()
    weapon.use()
    armor.defend()
    print()


warrior_th = threading.Thread(target=initiate_character, args=(WarriorFactory(),))
mage_th = threading.Thread(target=initiate_character, args=(MageFactory(),))

warrior_th.start()
mage_th.start()

warrior_th.join()
mage_th.join()

print("\nAll threads finished successfully\n")