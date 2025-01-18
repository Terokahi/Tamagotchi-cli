import os

import gameFiles.res as res

health = ["Health", 100]
hunger = ["Hunger", 100]
fun = ["Fun", 100]
energy = ["Energy", 100]

stats = [health, hunger, fun, energy]

def mod_stat(stat):
    """
    mods the given stat by +50 and the rest -10
    """
    for i in range(len(stats)):
        if i == stat:
            stats[i][1] += 50
            if stats[i][1] >= 100:
                stats[i][1] = 100
        else:
            stats[i][1] += -5

            if stats[i][1] <= 0:
                death(i)

def const_mod_stat():
    for i in range(len(stats)):        
        stats[i][1] += -0.04
        
        if stats[i][1] <= 0:
            death(i)

def death(stat):
    os.system("clear")
    print(res.sprite_dead)

    match stat:
        case 0:
            print("your Tamagotchi died")
            quit()
        case 1:
            print("your Tamagotchi starved")
            quit()
        case 2:
            print("your Tamagotchi got bored to death")
            quit()
        case 3:
            print("your Tamagotchi didn't sleep enough and died")
            quit()