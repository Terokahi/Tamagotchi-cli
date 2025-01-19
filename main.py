import os
import time
import select
import sys

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.fmod as fmod
import gameFiles.prompts as prompts
import gameFiles.res as res

MENU_SLEEP_TIME = .8
GAME_SLEEP_TIME = .5



def non_blocking_input():
    """
    get a "un-blocked" input
    """
    print(prompts.interaction, end='', flush=True)  # Print prompt
    # Use select to determine if input is available
    ready, _, _ = select.select([sys.stdin], [], [], GAME_SLEEP_TIME)  # pause for .5 seconds
    if ready:
        return sys.stdin.readline().strip().lower()  # Read input
    else:
        Tamagotchi.const_mod_stat()



def start_loop():
    """
    This is the game loop
    """
    while True:
        os.system("clear")
        res.animation()

        # get input
        match non_blocking_input():
            case 'h':
                Tamagotchi.mod_stat(0)
            
            case 'f':
                Tamagotchi.mod_stat(1)
            
            case 'p':
                Tamagotchi.mod_stat(2)
            
            case 's':
                Tamagotchi.mod_stat(3)
            
            case 't':
                pass

            case 'a':
                fmod.save_game()

            case 'x':
                break

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
            case 's':
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