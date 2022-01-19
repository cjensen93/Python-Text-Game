def rarity(item, new):
    if new == "Common":
        item.setArmorRating(item.getBaseArmorRating())
        item.setWeight(item.getBaseWeight())
        item.recalculateValue()
        item.setRarity("Common")
        return

    elif new == "Rare":
        item.setArmorRating(round(item.getBaseArmorRating() * 1.3))
        item.setWeight(round(item.getBaseWeight() * 1.2))
        item.recalculateValue()
        item.setValue((round(item.getValue() * 1.5)))
        item.setRarity("Rare")
        return

    elif new == "Legendary":
        item.setArmorRating(round(item.getBaseArmorRating() * 1.8))
        item.setWeight(round(item.getBaseWeight() * 1.3))
        item.recalculateValue()
        item.setValue((round(item.getValue() * 2.5)))
        item.setRarity("Legendary")
        return

    elif new == "Epic":
        item.setArmorRating(round(item.getBaseArmorRating() * 2.5))
        item.setWeight(round(item.getBaseWeight() * 1.4))
        item.recalculateValue()
        item.setValue((round(item.getValue() * 4)))
        item.setRarity("Epic")
        return
