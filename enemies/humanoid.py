from random import randint
from enemies import enemyClass


def bandit():
    name = "Bandit"
    style = "Human"
    level = randint(5, 10)
    health = (randint(70, 90) + round(level * 2.5))
    attackLow = (randint(5, 7) + level)
    attackHigh = (randint(12, 15) + level)
    defense = randint(50, 60)
    speed = randint(80, 85)
    xp = (100 + (level * 5))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy


def knight():
    name = "Knight"
    style = "Human"
    level = randint(20, 25)
    health = (randint(150, 180) + (level * 4))
    attackLow = (randint(14, 18) + level)
    attackHigh = (randint(22, 25) + level)
    defense = randint(80, 90)
    speed = randint(30, 35)
    xp = (500 + (level * 50))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy


def sorcerer():
    name = "Sorcerer"
    style = "Human"
    level = randint(10, 15)
    health = (randint(60, 80) + (level * 2))
    attackLow = (randint(35, 45) + (round(level * 0.5)))
    attackHigh = (randint(55, 65) + (round(level * 0.5)))
    defense = randint(25, 30)
    speed = randint(40, 45)
    xp = (200 + (level * 50))
    enemy = enemyClass.Enemy(name, style, level, health, attackLow, attackHigh, defense, speed, xp)
    return enemy
