from enemies import creatures
from random import randint
from time import sleep


def setup():
    print("\033[93m" + "\nHere we will generate random enemies to fight." + "\033[0m")

    enemyOne = firstMenu()
    enemyTwo = secondMenu()
    combat(enemyOne, enemyTwo)


def firstMenu():
    while True:
        print("\n1 - Wolf\n2 - Bear\n3 - Dragon")
        firstSelection = input("Select the first creature to fight:   ")

        if firstSelection == "1":
            enemyOne = creatures.wolf()
            return enemyOne

        elif firstSelection == "2":
            enemyOne = creatures.bear()
            return enemyOne

        elif firstSelection == "3":
            enemyOne = creatures.dragon()
            return enemyOne

        else:
            print("\033[93m" + "Error: Incorrect Input" + "\033[0m")


def secondMenu():
    while True:
        print("\n1 - Wolf\n2 - Bear\n3 - Dragon")
        firstSelection = input("Select the second creature to fight:   ")

        if firstSelection == "1":
            enemyOne = creatures.wolf()
            return enemyOne

        elif firstSelection == "2":
            enemyOne = creatures.bear()
            return enemyOne

        elif firstSelection == "3":
            enemyOne = creatures.dragon()
            return enemyOne

        else:
            print("\033[93m" + "Error: Incorrect Input" + "\033[0m")


def attack(attacker, defender):
    attackBase = randint(attacker.getAttackLow(), attacker.getAttackHigh())
    defenseBase = defender.getDefense()
    attackModifier = attackBase / defenseBase
    attackActual = round(attackBase * attackModifier)
    return attackActual


def healthCheck(enemyOne, enemyTwo):
    keepFighting = 0
    if enemyOne <= 0:
        keepFighting += 1
    if enemyTwo <= 0:
        keepFighting += 1

    if keepFighting == 0:
        return True

    else:
        return False


def combat(enemyOne, enemyTwo):
    one = "\033[94m" + enemyOne.getName() + "\033[0m"
    two = "\033[92m" + enemyTwo.getName() + "\033[0m"
    print(f"\nYou have chosen {one} and {two} to fight!")

    turnCounter = 0

    if enemyOne.getSpeed() >= enemyTwo.getSpeed():
        print(f"{one} will initiate attack, because of its greater speed.")

    else:
        print(f"{two} will initiate attack, because of its greater speed.")
        turnCounter += 1

    enemyOneHealth = enemyOne.getHealth()
    enemyTwoHealth = enemyTwo.getHealth()

    while healthCheck(enemyOneHealth, enemyTwoHealth):
        if (turnCounter % 2) == 0:
            engage = attack(enemyOne, enemyTwo)
            enemyTwoHealth -= engage
            print(f"{one} did {engage} damage to {two}, who has {enemyTwoHealth} health left.")
            turnCounter += 1
            sleep(0.5)

        elif (turnCounter % 2) == 1:
            engage = attack(enemyTwo, enemyOne)
            enemyOneHealth -= engage
            print(f"{two} did {engage} damage to {one}, who has {enemyOneHealth} health left.")
            turnCounter += 1
            sleep(0.5)

    if enemyOneHealth <= 0:
        print(f"\n{two} defeated {one}!")

    else:
        print(f"\n{one} defeated {two}")
