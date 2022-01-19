from random import randint
from armor import armorClass


def leatherBoots():
    name = "Leather Boots"
    baseArmorRating = randint(4, 6)
    baseWeight = randint(2, 14)
    value = round((baseArmorRating * 10) / baseWeight)
    rarity = "Common"
    item = armorClass.Armor(name, baseArmorRating, baseWeight, value, rarity)
    return item
