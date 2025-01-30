"""
Nothing here besides all the sprites used Modify the sprites as you see fit

To display a animation put the sprites into the array "sprite_idle[]"
the function "animation()" will do the magic work of printing them at the right time
"""
import time

import gameFiles.Tamagotchi as Tamagotchi
import gameFiles.prompts as prompts

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

CURSOR_UP = "\033[1A"
CLEAR = "\x1b[2K"

def animation():
  # get the current sprite to display
  global sprite_disp

  # reset Sprite if end of the sprite array was reached
  if sprite_disp == len(sprite_idle):
      sprite_disp = 0
  print(prompts.interaction)

  # output the stats
  for stat in Tamagotchi.stats:
      print(f"{stat[0]}\t: {stat[1]:.0f}")
  
  # output the current "Frame"
  print(sprite_idle[sprite_disp], end="\r")
  for i in range(17):
    print(CURSOR_UP + CLEAR, end="")

  # raise this to show the next sprite
  sprite_disp += 1
  time.sleep(0.5)
