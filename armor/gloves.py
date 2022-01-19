from random import randint
from armor import armorClass


def leatherGloves():
    name = "Leather Gloves"
    baseArmorRating = randint(2, 4)
    baseWeight = randint(1, 2)
    value = round((baseArmorRating * 5))
    rarity = "Common"
    item = armorClass.Armor(name, baseArmorRating, baseWeight, value, rarity)
    return item
