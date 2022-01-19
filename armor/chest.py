from random import randint
from armor import armorClass


def leatherChestPiece():
    name = "Leather Chest Piece"
    baseArmorRating = randint(18, 24)
    baseWeight = randint(8, 11)
    value = round((baseArmorRating * 12) / baseWeight)
    rarity = "Common"
    item = armorClass.Armor(name, baseArmorRating, baseWeight, value, rarity)
    return item
