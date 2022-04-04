class Location:
    def __init__(self, name, region, levelAbove, levelBelow):
        self.name = name
        self.region = region
        self.levelAbove = levelAbove
        self.levelBelow = levelBelow

    # --------------
    # Getter Methods
    # --------------
    def getName(self):
        return self.name

    def getRegion(self):
        return self.region

    def getLevelAbove(self):
        return self.levelAbove

    def getLevelBelow(self):
        return self.levelBelow

    def getAll(self):
        allString = str(self.name) + " -"
        allString += "\nRegion: " + str(self.region)
        allString += "\nLevels Above:"
        for i in range(len(self.levelAbove)):
            allString += "\n- " + str(self.levelAbove[i])
        allString += "\nLevels Below:"
        for j in range(len(self.levelBelow)):
            allString += "\n- " + str(self.levelBelow[j])
        return allString

    # --------------
    # Setter Methods
    # --------------
    def setName(self, new):
        self.name = new

    def setRegion(self, new):
        self.region = new

    def setLevelAbove(self, new):
        self.levelAbove = new

    def setLevelBelow(self, new):
        self.levelBelow = new