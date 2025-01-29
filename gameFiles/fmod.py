import os
from os import path, listdir
import pickle
import time

import gameFiles.Items as Items
import gameFiles.Tamagotchi as Tamagotchi

# save file ending
# save folder
f_end = "Tamago.dat"
fI_end = "Items.dat"
sav_dir = "Saves/"

def load_game():
    """
    load the given save if it exists
    """
    # print all of the existing save files
    sav_files = listdir(sav_dir)
    print("Existing saves: ")
    for file in sav_files:
        print(file)

    sav_name = input("Give File Name you want to start: ")
    # try to open the file with the given file Name
    try:
        sav_load = open(sav_dir+sav_name+"/"+f_end, "br")
        Tamagotchi.stats = pickle.load(sav_load)
        sav_load.close()

        sav_load = open(sav_dir+sav_name+"/"+fI_end, "br")
        Items.itemLst = pickle.load(sav_load)
        sav_load.close()
        # return flag to show load was succesful
        return True
    # The file doesn't exist don't do nothing
    except:
        print("File doesn't exist")
        time.sleep(.5)
        

def del_game():
    """
    delete a save file according to the user
    """
    # print all of the existing save files
    sav_files = listdir(sav_dir)
    print("Existing saves: ")
    for file in sav_files:
        print(file)
    
    sav_name = input("Give File Name you want to delete: ")
    # try to delete the user given file otherwise inform the user
    try:
        os.remove(sav_dir+sav_name)
        return True
    except:
        print("file couldn't be deleted, it doesn't exist")
        

def save_game():
    """
    save the game
    """
    # print all of the existing save files
    sav_files = listdir(sav_dir)
    print("Existing saves: ")
    for file in sav_files:
        print(file)
    
    # get the File name, open it and save the Tamagotchis stats and Items to it
    sav_name = input("Give File Name you want to use or create: ")
    # try to create the file
    try:
        os.makedirs(sav_dir+sav_name)
    # excpetion File exists
    except:
        pass
    # Save the Stats
    sav = open(sav_dir+sav_name+"/"+f_end, "bw")
    pickle.dump(Tamagotchi.stats, sav)
    sav.close()
    # Save the Items
    sav = open(sav_dir+sav_name+"/"+fI_end, "bw")
    pickle.dump(Items.itemLst, sav)
    sav.close()
