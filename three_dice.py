# three_dice.py: writes the sum of three random integers between 1 and 6, such
# as you might get when rolling three dice.

import random
import stdio

x = random.randrange(1, 7)
y = random.randrange(1, 7)
z = random.randrange(1, 7)
stdio.writeln(x + y + z)
