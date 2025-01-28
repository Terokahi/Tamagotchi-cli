import os
import time
import threading

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.fmod as fmod
import gameFiles.prompts as prompts
import gameFiles.res as res

MENU_SLEEP_TIME = 1
GAME_SLEEP_TIME = .5

glob_timer = 0

class InputThread(threading.Thread):
    def __init__(self):
        """
        Initializes the input thread for handling user inputs asynchronously.
        """
        super(InputThread, self).__init__()
        self.daemon = True
        self.lastUserInput = ""


    def run(self):
        """
        Continuously receives user input and performs actions based on input.
        """
        while True:
            self.lastUserInput = input(prompts.interaction).lower()
            match self.lastUserInput:
                case 'a':
                    # Save the game state
                    fmod.save_game()

                case 'f':
                    # Modify hunger stat
                    Tamagotchi.mod_stat(1)

                case 'h':
                    # Modify health stat
                    Tamagotchi.mod_stat(0)

                case 'i':
                    # Placeholder for inventory
                    print("THE INVENTORY WILL BE HERE!!! (WIP)")
                    time.sleep(1.5)

                case 'p':
                    # Modify fun stat
                    Tamagotchi.mod_stat(2)

                case 's':
                    # Modify sleep stat
                    Tamagotchi.mod_stat(3)

                case 't':
                    # Placeholder for store
                    print("THE STORE WILL BE HERE!!! (WIP)")
                    threading.main_thread()
                    time.sleep(1.5)

                case 'x':
                    # Exit the loop
                    break

def gameLoop():
    """
    Main game loop that handles the game logic and updates.
    """
    global glob_timer
    asyncInput = InputThread()
    asyncInput.start()
    while True:
        print(prompts.interaction)
        res.animation()

        if glob_timer % 2:
            # Periodically modify stats
            Tamagotchi.const_mod_stat()
            if glob_timer == 200:
                glob_timer = 0

        if asyncInput.lastUserInput == 'x':
            # Exit the game loop
            asyncInput.join()
            break

        glob_timer += 0.5
        time.sleep(GAME_SLEEP_TIME)
        os.system('clear')

def main():
    """
    Main menu loop for starting, loading, and managing the game.
    """
    while True:
        os.system("clear")

        print(res.title)
        choice = input(prompts.menu).lower()
        os.system("clear")

        match choice:
            case 's':
                # Start a new game
                for stat in range(len(Tamagotchi.stats)):
                    Tamagotchi.stats[stat][1] = 100
                print("New Game")
                time.sleep(MENU_SLEEP_TIME)
                gameLoop()

            case 'l':
                # Load a game
                loadFlag = fmod.load_game()
                if loadFlag:
                    print("Load a Save")
                    time.sleep(MENU_SLEEP_TIME)
                    gameLoop()

            case 'd':
                # Delete a game
                delFlag = fmod.del_game()
                if delFlag:
                    print("Delete a Save")
                time.sleep(MENU_SLEEP_TIME)

            case 'o':
                # Show options
                print("These are the options!")
                time.sleep(MENU_SLEEP_TIME)

            case 'x':
                # Quit the game
                print("Goodbye")
                time.sleep(MENU_SLEEP_TIME)
                exit()

            case _:
                # Handle invalid input
                print("Invalid Input")
                time.sleep(MENU_SLEEP_TIME)
                continue

if __name__ == "__main__":
    os.system("clear")
    main()

