import gameFiles.Tamagotchi as Tamagotchi

sprite ="""
  .^._.^.
  | . . |
  ('---')
 .'     '.
 |/     \|
  \ /-\ /
   V   V
"""
sprite_left_left = """
  .^._.^.
  | . . |
 ( '---' )
 .'     '.
 |/     \|
 | /-\ -/
 |/   |/
"""

sprite_left = """
  .^._.^.
  | . . |
 ( '---' )
 .'     '.
 |/     \|
 | /-\ -/
 |/   |/
"""
sprite_right = """
  .^._.^.
  | . . |
 ( '---' )
 .'     '.
 |/     \|
  \- /-\ |
   \|   \|
"""

sprite_dead ="""
  .^._.^.
  | x x |
  (.---.)
 .'     '.
 |/     \|
  \ /-\ /
   V   V
"""

sprite_idle = [
    sprite_left,
    sprite,
    sprite_right
]

title = """
 _                                    _       _     _ 
| |                                  | |     | |   (_)
| |_ __ _ _ __ ___   __ _  __ _  ___ | |_ ___| |__  _ 
| __/ _` | '_ ` _ \ / _` |/ _` |/ _ \| __/ __| '_ \| |
| || (_| | | | | | | (_| | (_| | (_) | || (__| | | | |
 \__\__,_|_| |_| |_|\__,_|\__, |\___/ \__\___|_| |_|_|
                           __/ |                      
                          |___/                       
"""

sprite_disp = 0

def animation():
    global sprite_disp

    # reset Sprite
    if sprite_disp == len(sprite_idle):
        sprite_disp = 0
        
    print(sprite_disp)
    print(sprite_idle[sprite_disp])
    for stat in Tamagotchi.stats:
        print(f"{stat[0]}\t: {stat[1]:.0f}")
    sprite_disp += 1

