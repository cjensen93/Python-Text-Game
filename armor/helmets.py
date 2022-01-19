from random import randint
from armor import armorClass


def leatherHelmet():
    name = "Leather Helmet"
    baseArmorRating = randint(5, 7)
    baseWeight = randint(2, 4)
    value = round((baseArmorRating * 10) / baseWeight)
    rarity = "Common"
    item = armorClass.Armor(name, baseArmorRating, baseWeight, value, rarity)
    return item
