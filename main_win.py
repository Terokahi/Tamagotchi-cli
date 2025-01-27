import tkinter as tk
import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.res as res

# Flag to indicate changes in stats
change = False

# This creates the Main Window
# It contains the stat labels and interacts with user inputs
class App(tk.Tk):
    """Main application window for the Tamagotchi game."""
    
    def __init__(self):
        """Initialize the application window, variables, and UI components."""
        super().__init__()
        global change

        self.title('Tamamochi')

        # Initialize stat variables
        self.healthVar = tk.StringVar(self, Tamagotchi.stats[0])
        self.hungerVar = tk.IntVar(self, Tamagotchi.stats[1])
        self.funVar = tk.IntVar(self, Tamagotchi.stats[2])
        self.energyVar = tk.IntVar(self, Tamagotchi.stats[3])

        # Setup animation and labels
        self.animation = Animation(self)
        self.health = tk.Label(self, textvariable=self.healthVar)
        self.hunger = tk.Label(self, textvariable=self.hungerVar)
        self.fun = tk.Label(self, textvariable=self.funVar)
        self.energy = tk.Label(self, textvariable=self.energyVar)
        
        # List of stat variables
        self.stats = [self.healthVar, self.hungerVar, self.funVar, self.energyVar]

        # Pack the labels
        self.health.pack()
        self.hunger.pack()
        self.fun.pack()
        self.energy.pack()

        # Setup input buttons
        self.input = Input(self)
        
        # Update stats if there are changes
        if change == True:
            self.update()
            change = False

        # Start the main loop
        self.mainloop()

    def mod(self, stat):
        """Modify the given stat and update the UI."""
        Tamagotchi.mod_stat(stat)
        self.healthVar.set(Tamagotchi.stats[0])
        self.hungerVar.set(Tamagotchi.stats[1])
        self.funVar.set(Tamagotchi.stats[2])
        self.energyVar.set(Tamagotchi.stats[3])

# Handles animations in a separate thread to avoid interference with the main loop
class Animation(tk.Frame):
    """Animation handler for the Tamagotchi character."""
    
    def __init__(self, parent):
        """Initialize the animation frame and display the initial sprite."""
        super().__init__(parent)
        self.pack()

        # Setup sprite variable and label
        self.sprites = tk.StringVar(self, res.sprite_idle[0])
        self.sprite = tk.Label(self, textvariable=self.sprites, font='TkFixedFont')
        self.sprite.pack()

# Handles all button Inputs for user interactions
class Input(tk.Frame):
    """Input handler for user interaction buttons."""
    
    def __init__(self, parent):
        """Initialize input buttons for interacting with Tamagotchi."""
        global change
        # Setup buttons for different actions
        self.healthBtn = tk.Button(parent, text='Heal', command=lambda: parent.mod(0))
        self.hungerBtn = tk.Button(parent, text='Feed', command=lambda: parent.mod(1))
        self.funBtn = tk.Button(parent, text='Play', command=lambda: parent.mod(2))
        self.sleepBtn = tk.Button(parent, text='Sleep', command=lambda: parent.mod(3))
        
        # Pack buttons
        self.healthBtn.pack(side='left')
        self.hungerBtn.pack(side='left')
        self.funBtn.pack(side='left')
        self.sleepBtn.pack(side='left')

if __name__ == '__main__':
    # Create and run the application
    app = App()
    # main()

