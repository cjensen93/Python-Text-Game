from locations import locationClass
from locations import destinationClass

def SmokeHill():
    name = "Smoke Hill"
    region = "Iron Band"
    levelAbove = ["Iron Band", "Murkshire", "Capitol Lands"]
    levelBelow = [destinationClass.Destination("Rusty Tavern",
                                               "A small, dark tavern in the center of town",
                                               ["John Smith, Jane Doe"],
                                               "Smoke Hill"),
                  destinationClass.Destination("Town Square",
                                               "The central market point for the old town",
                                               ["Princess Jane", "Archmage Duke"],
                                               "Smoke Hill"),
                  destinationClass.Destination("Forge of Dawn",
                                               "This massive forge is the central business in all of Smoke Hill",
                                               ["Forgemaster Bill", "Protege Fiona"],
                                               "Smoke Hill")]
    return locationClass.Location(name, region, levelAbove, levelBelow)