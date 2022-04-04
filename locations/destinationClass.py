class Destination:
    def __init__(self, name, description, occupants, levelAbove):
        self.name = name
        self.description = description
        self.occupants = occupants
        self.levelAbove = levelAbove

    # --------------
    # Getter Methods
    # --------------
    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getOccupants(self):
        return self.occupants

    def getLevelAbove(self):
        return self.levelAbove

    # --------------
    # Setter Methods
    # --------------
    def setName(self, new):
        self.name = new

    def setDescription(self, new):
        self.description = new

    def setOccupants(self, new):
        self.occupants = new

    def setLevelAbove(self, new):
        self.levelAbove = new
