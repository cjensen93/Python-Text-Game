from random import randint
from weapons import weaponClass


def ironBroadsword():
    name = "Iron Broadsword"
    attackLow = randint(10, 14)
    attackHigh = randint(18, 22)
    critical = randint(5, 10)
    weight = randint(6, 8)
    value = round((attackLow * attackHigh / weight))
    rarity = "Common"
    item = weaponClass.Blades(name, attackLow, attackHigh, critical, weight, value, rarity)
    return item


def ironLongsword():
    name = "Iron Longsword"
    attackLow = randint(8, 11)
    attackHigh = randint(15, 17)
    critical = randint(11, 15)
    weight = randint(3, 5)
    value = round((attackLow * attackHigh / weight))
    rarity = "Common"
    item = weaponClass.Blades(name, attackLow, attackHigh, critical, weight, value, rarity)
    return item


def ironDagger():
    name = "Iron Dagger"
    attackLow = randint(4, 7)
    attackHigh = randint(9, 12)
    critical = randint(21, 30)
    weight = 1
    value = attackLow * attackHigh
    rarity = "Common"
    item = weaponClass.Blades(name, attackLow, attackHigh, critical, weight, value, rarity)
    return item
