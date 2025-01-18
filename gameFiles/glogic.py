import gameFiles.Tamagotchi as Tamagotchi

def choice(sym):
    match sym:
        case 'h':
            return Tamagotchi.mod_stat(0)
        case 'f':
            return Tamagotchi.mod_stat(1)
        case 'p':
            return Tamagotchi.mod_stat(2)
        case 's':
            return Tamagotchi.mod_stat(3)
        case 't':
            pass
        case 'a':
            pass
        case 'x':
            quit()
        case _:
            return ""