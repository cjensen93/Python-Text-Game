from random import randint
from armor import armorClass


def leatherPants():
    name = "Leather Pants"
    baseArmorRating = randint(11, 14)
    baseWeight = randint(5, 7)
    value = round((baseArmorRating * 10) / baseWeight)
    rarity = "Common"
    item = armorClass.Armor(name, baseArmorRating, baseWeight, value, rarity)
    return item
