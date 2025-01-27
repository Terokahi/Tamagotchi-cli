import os
import time
import threading

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.fmod as fmod
import gameFiles.prompts as prompts
import gameFiles.res as res

MENU_SLEEP_TIME = .8
GAME_SLEEP_TIME = .5

glob_timer = 0

class InputThread(threading.Thread):
    def __init__(self):
        super(InputThread, self).__init__()
        self.daemon = True
        self.lastUserInput = ""

    def run(self):
        """
        This is the game loop
        """
        while True:
            os.system('clear')
            # get input
            self.lastUserInput = input()
            match self.lastUserInput.lower(): # non_blocking_input():
                case 'a':
                    fmod.save_game()

                case 'f':
                    Tamagotchi.mod_stat(1)  

                case 'h':
                    Tamagotchi.mod_stat(0)

                case 'i':
                    print("THE INVENTORY WILL BE HERE!!! (WIP)")
                    time.sleep(1.5)

                case 'p':
                    Tamagotchi.mod_stat(2)
                
                case 's':
                    Tamagotchi.mod_stat(3)
                
                case 't':
                    print("THE STORE WILL BE HERE!!! (WIP)")
                    time.sleep(1.5)

                case 'x':
                    break

def gameLoop():
    global glob_timer
    asyncInput = InputThread()
    asyncInput.start()
    while True:
        print(prompts.interaction)
        res.animation()
        print(asyncInput.lastUserInput)

        if glob_timer == 5:
            Tamagotchi.const_mod_stat()

        if asyncInput.lastUserInput == 'x':
            asyncInput.join()
            break
        glob_timer += 0.5
        os.system('clear')

def main():
    """
    This is the Main Menu Loop
    """
    gameThread = InputThread()
    while True:
        os.system("clear")

        print(res.title)
        choice = input(prompts.menu).lower()
        os.system("clear")

        match choice:
            case 's':
                # start a new game
                for stat in range(len(Tamagotchi.stats)):
                    Tamagotchi.stats[stat][1] = 100
                print("New Game")
                time.sleep(MENU_SLEEP_TIME)    
                gameLoop()

            case 'l':
                # load a game
                loadFlag = fmod.load_game()
                if loadFlag:
                    print("Load a Save")            
                    time.sleep(MENU_SLEEP_TIME)
                    gameLoop()

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
    os.system("clear")
    main()
