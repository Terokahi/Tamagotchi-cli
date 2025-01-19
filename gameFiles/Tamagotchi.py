import os
import random as rng

import gameFiles.res as res

MAX_GAIN = 40
MIN_GAIN = 20

MAX_LOSS = -.25
MIN_LOSS = 0

health = ["Health", 100.0]
hunger = ["Hunger", 100.0]
fun = ["Fun", 100.0]
energy = ["Energy", 100.0]

stats = [health, hunger, fun, energy]

def mod_stat(stat):
    """
    mods the given stat by +50 and the rest -10
    Todo: modifiers
    """
    for i in range(len(stats)):
        if i == stat:
            stats[i][1] += rng.uniform(MIN_GAIN, MAX_GAIN)
            if stats[i][1] >= 100:
                stats[i][1] = 100
        else:
            stats[i][1] += -5

            if stats[i][1] <= 0:
                death(i)

def const_mod_stat():
    """
    Constantly mod the stats of the Tamagotchi
    Todo: modifiers
    """
    for i in range(len(stats)):        
        stats[i][1] += round(rng.uniform(MIN_LOSS, MAX_LOSS), 2)
        
        if stats[i][1] <= 0:
            death(i)

def death(stat):
    """
    call to print the proper death statement
    """
    os.system("clear")
    print(res.sprite_dead)

    match stat:
        case 0:
            # Health is 0
            print("your Tamagotchi died")
            quit()
        case 1:
            # Hunger is 0
            print("your Tamagotchi starved")
            quit()
        case 2:
            # Fun is 0
            print("your Tamagotchi got bored to death")
            quit()
        case 3:
            # Energy is 0
            print("your Tamagotchi didn't sleep enough and died")
            quit()
