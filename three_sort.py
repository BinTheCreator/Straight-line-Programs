# three_sort.py: Takes three integers as command-line arguments and prints
# them in ascending order, separated by spaces.

import stdio
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
m = min(x, y, z)
n = max(x, y, z)
a = x+y+z-m-n
stdio.writeln(str(m) + ' ' + str(a) + ' ' + str(n))
