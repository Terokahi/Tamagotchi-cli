import os
import time
import select
import sys
from configparser import ConfigParser

if os.system == "win32" or "win64":
    import msvcrt

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.fmod as fmod
import gameFiles.prompts as prompts
import gameFiles.res as res

fname = "config.ini"
cfg = ConfigParser()
cfg.read(fname)

MENU_SLEEP_TIME = cfg.getfloat("TIMING", "menu_sleep_time")
GAME_SLEEP_TIME = cfg.getfloat("TIMING", "game_sleep_time")


def clear_screen():
    if os.system == "win32" or "win64":
        os.system("cls")
    else:
        os.system("clear")


def non_blocking_input():
    """
    get a "un-blocked" input
    """
    print(prompts.interaction, end='', flush=True)  # Print prompt
    # Use select to determine if input is available
    if sys.platform == "win32" or "win64":
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key.decode("utf-8")
        else:
            Tamagotchi.const_mod_stat()
    else:
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
        clear_screen()
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
        time.sleep(GAME_SLEEP_TIME)
        clear_screen()

def main():
    """
    This is the Main Menu Loop
    """
    while True:
        clear_screen()

        print(res.title)
        choice = input(prompts.menu).lower()
        clear_screen()

        match choice:
            case 's':
                # start a new game
                for stat in range(len(Tamagotchi.stats)):
                    Tamagotchi.stats[stat][1] = 100
                print("New Game")
                time.sleep(MENU_SLEEP_TIME)
                start_loop()
                

            case 'l':
                # load a game
                loadFlag = fmod.load_game()
                if loadFlag:
                    print("Load a Save")            
                    time.sleep(MENU_SLEEP_TIME)
                    start_loop()

            case 'd':
                # delete a game
                delFlag = fmod.del_game()
                if delFlag:
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
    clear_screen()
    main()