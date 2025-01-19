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
    ready, _, _ = select.select([sys.stdin], [], [], 0)  # pause for .5 seconds
    if ready:
        time.sleep(GAME_SLEEP_TIME)
        return sys.stdin.readline().strip().lower()  # Read input
    else:
        time.sleep(GAME_SLEEP_TIME)
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
                print("THE STORE WILL BE HERE!!! (WIP)")
                time.sleep(1.5)

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
        choice = input(prompts.menu).lower()
        os.system("clear")

        match choice:
            case 's':
                # start a new game
                print("New Game")
                time.sleep(MENU_SLEEP_TIME)
                start_loop()
                

            case 'l':
                # load a game
                if fmod.load_game():
                    print("Load a Save")            
                    time.sleep(MENU_SLEEP_TIME)
                    start_loop()

            case 'd':
                # delete a game
                if fmod.del_game():
                    print("Delete a Save")
                time.sleep(MENU_SLEEP_TIME)

            case 'o':
                # show options (none as of now)
                print("These are options!")
                time.sleep(MENU_SLEEP_TIME)
            
            case 'x':
                # quit the game
                print("Goodbye")
                time.sleep(MENU_SLEEP_TIME)
                exit()
            
            case _:
                # input not valid
                print("Invalid Input")
                time.sleep(MENU_SLEEP_TIME)
                continue

if __name__ == "__main__":
    os.system("clear")
    main()
