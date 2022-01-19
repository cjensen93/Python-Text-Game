class Enemy:
    def __init__(self, name, style, level, health, attackLow, attackHigh, defense, speed, xp):
        self.name = name
        self.style = style
        self.level = level
        self.health = health
        self.attackLow = attackLow
        self.attackHigh = attackHigh
        self.defense = defense
        self.speed = speed
        self.xp = xp

    # --------------
    # Getter Methods
    # --------------
    def getName(self):
        return self.name

    def getStyle(self):
        return self.style

    def getLevel(self):
        return self.level

    def getHealth(self):
        return self.health

    def getAttackLow(self):
        return self.attackLow

    def getAttackHigh(self):
        return self.attackHigh

    def getDefense(self):
        return self.defense

    def getSpeed(self):
        return self.speed

    def getXP(self):
        return self.xp

    def getAll(self):
        allString = "Name: " + str(self.name)
        allString += "\nType: " + str(self.style)
        allString += "\nLevel: " + str(self.level)
        allString += "\nHealth: " + str(self.health)
        allString += "\nAttack: " + str(self.attackLow) + "-" + str(self.attackHigh)
        allString += "\nDefense: " + str(self.defense)
        allString += "\nSpeed: " + str(self.speed)
        allString += "\nXP Value: " + str(self.xp)
        return allString
