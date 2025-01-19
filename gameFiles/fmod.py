import os
from os import path, listdir
import pickle
import time

import gameFiles.Tamagotchi as Tamagotchi

# save file ending
# save folder
f_end = ".dat"
sav_dir = "Saves/"

def load_game():
    """
    load the given save if it exists
    """
    # print all of the existing save files
    sav_files = [f for f in listdir(sav_dir) if path.isfile(path.join(sav_dir, f))]
    for file in sav_files:
        print(file[:-len(f_end)])

    sav_name = input("Give File Name you want to start: ")
    # try to open the file with the given file Name
    try:
        sav_load = open(sav_dir+sav_name+f_end, "br")
        Tamagotchi.stats = pickle.load(sav_load)
        sav_load.close()
        # return flag to show load was succesful
        return True
    except:
        print("File doesn't exist")
        time.sleep(.5)
        

def del_game():
    """
    delete a save file according to the user
    """
    # print all of the existing save files
    sav_files = [f for f in listdir(sav_dir) if path.isfile(path.join(sav_dir, f))]
    for file in sav_files:
        print(file[:-4])
    
    sav_name = input("Give File Name you want to delete: ")
    # try to delete the user given file otherwise inform the user
    try:
        os.remove(sav_dir+sav_name+f_end)
        return True
    except:
        print("file couldn't be deleted, it doesn't exist")
        

def save_game():
    """
    save the game
    """
    # print all of the existing save files
    sav_files = [f for f in listdir(sav_dir) if path.isfile(path.join(sav_dir, f))]
    for file in sav_files:
        print(file[:-4])
    
    # get the File name, open it and save the Tamagotchis stats to it
    sav_name = input("Give File Name you want to use or create: ")
    sav = open(sav_dir+sav_name+f_end, "bw")
    pickle.dump(Tamagotchi.stats, sav)
    sav.close()
