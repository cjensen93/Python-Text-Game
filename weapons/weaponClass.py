class Blades:
    def __init__(self, name, attackLow, attackHigh, critical, weight, value, rarity):
        self.type = "Melee Weapon"
        self.name = name
        self.baseAttackLow = attackLow
        self.baseAttackHigh = attackHigh
        self.attackLow = self.baseAttackLow
        self.attackHigh = self.baseAttackHigh
        self.baseCritical = critical
        self.critical = self.baseCritical
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

    def getBaseAttackLow(self):
        return self.baseAttackLow

    def getBaseAttackHigh(self):
        return self.baseAttackHigh

    def getAttackLow(self):
        return self.attackLow

    def getAttackHigh(self):
        return self.attackHigh

    def getBaseCritical(self):
        return self.baseCritical

    def getCritical(self):
        return self.critical

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
        allString += "\nAttack: " + str(self.attackLow) + " - " + str(self.attackHigh)
        allString += "\nCritical: " + str(self.critical) + "%"
        allString += "\nWeight: " + str(self.weight)
        allString += "\nValue: " + str(self.value) + " Gold"
        allString += "\nRarity: " + str(self.rarity)
        return allString

    # --------------
    # Setter Methods
    # --------------
    def setName(self, new):
        self.name = new

    def setAttackLow(self, new):
        self.attackLow = new

    def setAttackHigh(self, new):
        self.attackHigh = new

    def setCritical(self, new):
        self.critical = new

    def setWeight(self, new):
        self.weight = new

    def setValue(self, new):
        self.value = new

    def setRarity(self, new):
        self.rarity = new

    def recalculateValue(self):
        self.value = round((self.attackLow * self.attackHigh) / self.weight)
