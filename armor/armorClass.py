class Armor:
    def __init__(self, name, armor, weight, value, rarity):
        self.type = "Armor"
        self.name = name
        self.baseArmorRating = armor
        self.armorRating = self.baseArmorRating
        self.baseWeight = weight
        self.weight = self.baseWeight
        self.value = value
        self.rarity = rarity

    # --------------
    # Getter Methods
    # --------------
    def getType(self):
        return self.type

    def getName(self):
        return self.name

    def getBaseArmorRating(self):
        return self.baseArmorRating

    def getArmorRating(self):
        return self.armorRating

    def getBaseWeight(self):
        return self.baseWeight

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def getRarity(self):
        return self.rarity

    def getAll(self):
        allString = str(self.name) + " -"
        allString += "\nArmor Rating: " + str(self.armorRating)
        allString += "\nWeight: " + str(self.weight)
        allString += "\nValue: " + str(self.value) + " Gold"
        allString += "\nRarity: " + str(self.rarity)
        return allString

    # --------------
    # Setter Methods
    # --------------
    def setName(self, new):
        self.name = new

    def setArmorRating(self, new):
        self.armorRating = new

    def setWeight(self, new):
        self.weight = new

    def setValue(self, new):
        self.value = new

    def setRarity(self, new):
        self.rarity = new

    def recalculateValue(self):
        self.value = round((self.baseArmorRating * 12) / self.weight)
