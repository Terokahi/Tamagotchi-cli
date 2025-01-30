
class Items:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.desc = ""
        
        self.effect = [None, None, None, None] # Health, Hunger, Fun, Energy

        self.invent = False

"""
#--------------------------------------------------------------------------------------------------------------------------------#
#------------------------------------- Standard Layout for Item creation --------------------------------------------------------#
#--------------------------------------------------------------------------------------------------------------------------------#
# create The Item as class item
* Item = Items()

# Give the Item the name you want
# String
* Item.name = name

# How much the player should pay for the item
# Int
* Item.price = price

# Short description of the item, do or do not specify what it does
# String
* Item.desc = Description

# modify the effects of the item
# All given in Float/Int
* Item.effect = [health, Hunger, Fun, Energy]

# it shouldn't be modified because the Item isn't neccesarily already in the Inventory
# upon creation, If it is supposed to be you may set it to True
# Given in Bool
* Item.invent = should not be modified
"""
# std layout for Item creation
wood = Items()
wood.name = "Wood"
wood.price = 5
wood.desc = "\tIt's a piece of Wood might be fun to play with... looks heavy though"

wood.effect[0] = 0
wood.effect[1] = 0
wood.effect[2] = 0.75
wood.effect[3] = -0.25

itemLst = [wood]