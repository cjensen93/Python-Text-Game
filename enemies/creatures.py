from random import randint
from enemies import enemyClass


def wolf():
    name = "Wolf"
    style = "Creature"
    level = randint(3, 8)
    health = (randint(25, 32) + (level * 2))
    attackLow = (randint(2, 5) + level)
    attackHigh = (randint(7, 10) + level)
    defense = randint(20, 30)
    speed = randint(60, 75)
    xp = (50 + (level * 5))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy


def bear():
    name = "Bear"
    style = "Creature"
    level = randint(5, 10)
    health = (randint(80, 100) + (level * 3))
    attackLow = (randint(8, 12) + level)
    attackHigh = (randint(16, 20) + level)
    defense = randint(60, 70)
    speed = randint(30, 40)
    xp = (200 + (level * 10))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy


def dragon():
    name = "Dragon"
    style = "Creature"
    level = randint(50, 60)
    health = (randint(200, 250) + (level * 5))
    attackLow = (randint(45, 60) + (round(level * 0.5)))
    attackHigh = (randint(80, 90) + (round(level * 0.5)))
    defense = (randint(110, 125) + level)
    speed = randint(30, 40)
    xp = (500 + (level * 200))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy
