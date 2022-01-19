def rarity(item, new):
    if new == "Common":
        item.setAttackLow(item.getBaseAttackLow())
        item.setAttackHigh(item.getBaseAttackHigh())
        item.setCritical(item.getCritical())
        item.setWeight(item.getBaseWeight())
        item.recalculateValue()
        item.setRarity("Common")
        return

    elif new == "Rare":
        item.setAttackLow(round(item.getBaseAttackLow() * 1.3))
        item.setAttackHigh(round(item.getBaseAttackHigh()) * 1.3)
        item.setCritical(round(item.getCritical() * 1.1))
        item.setWeight(item.getBaseWeight() + 1)
        item.recalculateValue()
        item.setValue(round(item.getValue() * 1.5))
        item.setRarity("Rare")
        return

    elif new == "Legendary":
        item.setAttackLow(round(item.getBaseAttackLow() * 1.8))
        item.setAttackHigh(round(item.getBaseAttackHigh()) * 1.8)
        item.setCritical(round(item.getCritical() * 1.25))
        item.setWeight(item.getBaseWeight() + 2)
        item.recalculateValue()
        item.setValue(round(item.getValue() * 2.5))
        item.setRarity("Legendary")
        return

    elif new == "Epic":
        item.setAttackLow(round(item.getBaseAttackLow() * 2.5))
        item.setAttackHigh(int(round(item.getBaseAttackHigh()) * 2.5))
        item.setCritical(round(item.getCritical() * 1.5))
        item.setWeight(item.getBaseWeight() + 3)
        item.recalculateValue()
        item.setValue(round(item.getValue() * 4))
        item.setRarity("Legendary")
        return
