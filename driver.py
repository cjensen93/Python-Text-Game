from time import sleep
import armor.helmets
import armor.chest
import armor.gloves
import armor.pants
import armor.boots
import armor.armorClass
import armor.rarity
import weapons.blades
import weapons.weaponClass
import weapons.rarity
import enemies.creatures
import enemies.humanoid
import enemies.enemyClass
import combat.combat
import sys


yesList = ["Y", "y", "YES", "Yes", "yes"]
noList = ["N", "n", "NO", "No", "no"]


def startGame():
    welcomeMessage()
    while True:
        print("\nMAIN MENU")
        print("1 - Generate Character\n2 - Generate Enemy\n3 - Combat\n4 - Exit")
        menuOption = str(input("What would you like to do? (1,2,3):  "))

        if menuOption == "1":
            generateCharacter()

        if menuOption == "2":
            generateEnemy()

        if menuOption == "3":
            combat.combat.setup()

        elif menuOption == "4":
            print(Colors.HEADER + "\nThank you for playing!")
            sys.exit(0)

        else:
            print(Colors.WARNING + "Error: Enter 'Y' or 'N'\n" + Colors.ENDC)


def generateCharacter():
    print("\n\nHere we will generate your character.")
    sleep(1)
    firstHelm = armor.helmets.leatherHelmet()
    firstChest = armor.chest.leatherChestPiece()
    firstGloves = armor.gloves.leatherGloves()
    firstPants = armor.pants.leatherPants()
    firstBoots = armor.boots.leatherBoots()

    choice = 0
    weaponSelect = True
    while weaponSelect:
        print("\n1 = Broadsword\n2 = Longsword\n3 = Dagger")
        selection = str(input("Would you like a broadsword, longsword, or dagger? (1,2,3):  "))

        if selection == "1":
            choice = 1
            weaponSelect = False
        elif selection == "2":
            choice = 2
            weaponSelect = False
        elif selection == "3":
            choice = 3
            weaponSelect = False
        else:
            print(Colors.WARNING + "Error: Invalid Input" + Colors.ENDC)

    firstWeapon = None
    if choice == 1:
        firstWeapon = weapons.blades.ironBroadsword()
    if choice == 2:
        firstWeapon = weapons.blades.ironLongsword()
    if choice == 3:
        firstWeapon = weapons.blades.ironDagger()

    inventory = [firstHelm, firstChest, firstGloves, firstPants, firstBoots, firstWeapon]

    print(Colors.WARNING + "\nYou were given a set of Leather Armor that will get you by for now.\n" + Colors.ENDC)
    sleep(1)
    menu = True
    while menu:
        print(Colors.WARNING + "\n--------------------------------" + Colors.ENDC)
        print("1 = Check Inventory\n2 = Change Rarity Of Items\nE = Exit Game")
        selection = str(input("What would you like to do next? (1,2,E):  "))

        # CHECK INVENTORY MENU

        if selection == "1":
            inventoryMenu = True
            while inventoryMenu:
                print(Colors.WARNING + "\n--------------------------------" + Colors.ENDC)
                print("1 = Display all inventory\n2 = Check Equipped Armor\n3 = Check Equipped Weapon\n4 = Exit Menu")
                inventoryMenuSelection = str(input("Select an option (1,2,3,4):  "))

                if inventoryMenuSelection == "1":
                    print()
                    for i in inventory:
                        print(i.getName())

                elif inventoryMenuSelection == "2":
                    for i in range(len(inventory) - 1):
                        print()
                        print(inventory[i].getAll())

                    totalArmorRating = 0
                    for i in range(len(inventory) - 1):
                        totalArmorRating += inventory[i].getArmorRating()
                    print(Colors.OKCYAN + "\nTotal Armor Rating: " + str(totalArmorRating) + Colors.ENDC)

                elif inventoryMenuSelection == "3":
                    print()
                    print(inventory[5].getAll())

                elif inventoryMenuSelection == "4":
                    inventoryMenu = False
                    print()

                else:
                    print(Colors.WARNING + "Error: Invalid Input" + Colors.ENDC)

        # CHANGE RARITY MENU

        elif selection == "2":
            print("Too Bad")


def generateEnemy():
    print(Colors.WARNING + "\nHere we will generate random enemies." + Colors.ENDC)
    sleep(1)

    menuExit = False
    while not menuExit:
        print("\n1 - Wolf\n2 - Bear\n3 - Dragon\n4 - Bandit\n5 - Knight\n6 - Sorcerer\n7 - Exit")
        menuOption = input("What would you like to do? (1-7):   ")

        if menuOption == "1":
            enemy = enemies.creatures.wolf()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "2":
            enemy = enemies.creatures.bear()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "3":
            enemy = enemies.creatures.dragon()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "4":
            enemy = enemies.humanoid.bandit()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "5":
            enemy = enemies.humanoid.knight()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "6":
            enemy = enemies.humanoid.sorcerer()
            print(Colors.WARNING + "\n----------------------" + Colors.ENDC)
            print(f"{enemy.getAll()}")
            print(Colors.WARNING + "----------------------" + Colors.ENDC)

        elif menuOption == "7":
            menuExit = True

        else:
            print(Colors.WARNING + "Error: Invalid Input" + Colors.ENDC)


def welcomeMessage():

    print("\n\n\n")
    print(Colors.HEADER + "Welcome to" + Colors.ENDC)

    print()
    print(Colors.WARNING + "    ____          __   __")
    print("   / __ \ __  __ / /_ / /_   ____   ____  ")
    print("  / /_/ // / / // __// __ \ / __ \ / __ \ ")
    print(" / ____// /_/ // /_ / / / // /_/ // / / / ")
    print("/_/     \__, / \__//_/ /_/ \____//_/ /_/  ")
    print("       /____/                             ")

    print("    ____  ")
    print("   / __ \ __  __ ____   ____ _ ___   ____   ____   _____")
    print("  / / / // / / // __ \ / __ `// _ \ / __ \ / __ \ / ___/")
    print(" / /_/ // /_/ // / / // /_/ //  __// /_/ // / / /(__  ) ")
    print("/_____/ \__,_//_/ /_/ \__, / \___/ \____//_/ /_//____/  ")
    print("                     /____/ " + Colors.ENDC)
    print()

    print(Colors.HEADER + "By Caleb Jensen (2022)" + Colors.ENDC)
    print("\n\n\n")
    sleep(2)


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# if rarityMenuOption == 1:
#     if inventory[rarityMenuNumber].getType() == "Armor":
#         armor.rarity.rarity(inventory[rarityMenuNumber], "Common")
#     elif inventory[rarityMenuNumber].getType() == "Melee Weapon":
#         weapons.rarity.rarity(inventory[rarityMenuNumber], "Common")
#
# elif rarityMenuOption == 2:
#     if inventory[rarityMenuNumber].getType() == "Armor":
#         armor.rarity.rarity(inventory[rarityMenuNumber], "Rare")
#     elif inventory[rarityMenuNumber].getType() == "Melee Weapon":
#         weapons.rarity.rarity(inventory[rarityMenuNumber], "Rare")
#
# elif rarityMenuOption == 3:
#     if inventory[rarityMenuNumber].getType() == "Armor":
#         armor.rarity.rarity(inventory[rarityMenuNumber], "Legendary")
#     elif inventory[rarityMenuNumber].getType() == "Melee Weapon":
#         weapons.rarity.rarity(inventory[rarityMenuNumber], "Legendary")
#
# elif rarityMenuOption == 4:
#     if inventory[rarityMenuNumber].getType() == "Armor":
#         armor.rarity.rarity(inventory[rarityMenuNumber], "Epic")
#     elif inventory[rarityMenuNumber].getType() == "Melee Weapon":
#         weapons.rarity.rarity(inventory[rarityMenuNumber], "Epic")
