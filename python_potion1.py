# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:38:15 2023
@author: segal
"""
# practicing python:
# like with a project:
import random
    
health = 50 # character's health

# like setting it to 1 or more for a harder level, and a harder level can be 2 or 3. or more.

DifficultyLevel = 6

# that can mod how much the potion helps the player.

# then use a lib

# using pascel casing:
    
PotionHealth = int(random.randint(25,50) / DifficultyLevel) # and use casting to force it into an integer.

health += PotionHealth # adding a the random potion to the og health to the character.

# to see the new health after getting the random potion:
    
print(health)