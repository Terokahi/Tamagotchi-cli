import os
import time
import select
import sys
from multiprocessing import Process

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.glogic as logic
import gameFiles.fmod as fmod
import gameFiles.prompts as prompts
import gameFiles.res as res

MENU_SLEEP_TIME = .8
GAME_SLEEP_TIME = .5

frameAmount = len(res.sprite_idle) 
timer = 0
    
def non_blocking_input():
    """
    get a "un-blocked" input
    """
    print(prompts.interaction, end='', flush=True)  # Print prompt
    # Use select to determine if input is available
    ready, _, _ = select.select([sys.stdin], [], [], 0)  # Timeout after 2 seconds
    if ready:
        time.sleep(GAME_SLEEP_TIME)
        return sys.stdin.readline().strip()  # Read input
    else:
        time.sleep(GAME_SLEEP_TIME)
        Tamagotchi.const_mod_stat()


def start_loop():
    """
    This is the game loop
    """
    while True:
        os.system("clear")
        
        for sprite in res.sprite_idle:
            # display 
            print(sprite)

            for stat in Tamagotchi.stats:
                print(f"{stat[0]} :  {stat[1]:.1f}")

            logic.choice(non_blocking_input())
            os.system("clear")



def main():
    """
    This is the Main Menu Loop
    """
    while True:

        print(res.title)
        choice = input(prompts.menu)
        os.system("clear")

        match choice:
            case 'n':
                fmod.new_game()
                print("New Game")
                time.sleep(MENU_SLEEP_TIME)
                start_loop()
                

            case 'l':
                fmod.load_game()
                print("Load a Save")            
                time.sleep(MENU_SLEEP_TIME)
                start_loop()

            case 'd':
                fmod.del_game()
                print("Delete a Save")
                time.sleep(MENU_SLEEP_TIME)

            case 'o':
                print("These are options!")
                time.sleep(MENU_SLEEP_TIME)
            
            case 'x':
                print("Goodbye")
                time.sleep(MENU_SLEEP_TIME)
                exit()
            
            case _:
                print("Invalid Input")
                time.sleep(MENU_SLEEP_TIME)
                continue

if __name__ == "__main__":
    os.system("clear")
    main()