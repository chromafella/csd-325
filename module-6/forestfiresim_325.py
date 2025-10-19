"""Forest Fire Sim, modified by Sue Sampson, based on a program by Al Sweigart
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.
Inspired by Nicky Case's Emoji Sim http://ncase.me/simulating/model/
** use spaces, not indentation to modify **
Tags: short, bext, simulation

Module 5 MODDED
------------------------------------------------------
1) Added a WATER cell type that renders in BLUE with the character 'W'.
2) Placed a rectangular "lake" roughly in the center of the grid. The size
   is chosen to look close to the example; tweak LAKE_WIDTH/LAKE_HEIGHT to change.
3) Water is immutable and acts as a firebreak:
   - It never grows trees or gets struck by lightning.
   - It never becomes FIRE, and burning trees do not overwrite it.
   - Fire does not "cross" the water because spread logic only sets FIRE
     on neighboring TREE cells (water is not a TREE).
4) Documented all changes in this header and inline comments.
"""

import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

# Set up the constants:
WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = 'W'        # (NEW) water cell type

# (!) Try changing these settings to anything between 0.0 and 1.0:
INITIAL_TREE_DENSITY = 0.20  # Amount of forest that starts with trees.
GROW_CHANCE = 0.01           # Chance a blank space turns into a tree.
FIRE_CHANCE = 0.01           # Chance a tree is hit by lightning & burns.

# (!) Try setting the pause length to 1.0 or 0.0:
PAUSE_LENGTH = 0.5

# (NEW) Lake size; will be centered
LAKE_WIDTH = 15
LAKE_HEIGHT = 8


def main():
    forest = createNewForest()
    bext.clear()

    while True:  # Main program loop.
        displayForest(forest)

        # Run a single simulation step:
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    continue  # already set

                cell = forest[(x, y)]

                # (NEW) Water is immutable: copy and skip any growth/lightning/fire logic.
                if cell == WATER:
                    nextForest[(x, y)] = WATER
                    continue

                if (cell == EMPTY) and (random.random() <= GROW_CHANCE):
                    # Grow a tree in this empty space.
                    nextForest[(x, y)] = TREE
                elif (cell == TREE) and (random.random() <= FIRE_CHANCE):
                    # Lightning sets this tree on fire.
                    nextForest[(x, y)] = FIRE
                elif cell == FIRE:
                    # This tree is currently burning.
                    # Loop through all the neighboring spaces:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring TREES only.
                            # Water isn't a TREE, so it never ignites and blocks spread.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it:
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object (TREE or EMPTY):
                    nextForest[(x, y)] = cell

        forest = nextForest
        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """Returns a dictionary for a new forest data structure with a central lake."""
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # (kept) initial fill
            if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE  # Start as a tree.
            else:
                forest[(x, y)] = EMPTY  # Start as an empty space.

    # (NEW) Add a lake centered in the display. It overwrites whatever was there.
    cx = WIDTH // 2
    cy = HEIGHT // 2
    half_w = LAKE_WIDTH // 2
    half_h = LAKE_HEIGHT // 2
    lake_x0 = max(0, cx - half_w)
    lake_x1 = min(WIDTH - 1, cx + half_w)
    lake_y0 = max(0, cy - half_h)
    lake_y1 = min(HEIGHT - 1, cy + half_h)

    for lx in range(lake_x0, lake_x1 + 1):
        for ly in range(lake_y0, lake_y1 + 1):
            forest[(lx, ly)] = WATER

    return forest


def displayForest(forest):
    """Display the forest data structure on the screen (with blue water)."""
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            cell = forest[(x, y)]
            if cell == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif cell == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif cell == WATER:
                bext.fg('blue')  # water in blue
                print(WATER, end='')
            else:  # EMPTY
                print(EMPTY, end='')
        print()
    bext.fg('reset')  # Use the default font color.
    print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
    print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
    print('  Water = {} (blue) '.format(WATER), end='')
    print('Press Ctrl-C to quit.')


# If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.
