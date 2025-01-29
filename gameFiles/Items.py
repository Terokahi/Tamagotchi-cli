class Items:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.desc = ""
        
        self.effect = [None, None, None, None] # Health, Hunger, Fun, Energy

        self.invent = False

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