# great_circle.py: Takes four floats x1, y1, x2, and y2 representing the
# latitude and longitude in degrees of two points on earth as command-line
# arguments and prints the great-circle distance d (in km) between them,
# calculated as d=111arccos(sin(x1)sin(x2)+cos(x1)cos(x2)cos(y1-y2)).

import math
import stdio
import sys

x1 = math.radians(float(sys.argv[1]))
y1 = math.radians(float(sys.argv[2]))
x2 = math.radians(float(sys.argv[3]))
y2 = math.radians(float(sys.argv[4]))
d = (111 * math.degrees(math.acos(math.sin(x1)*math.sin(x2) +
     math.cos(x1)*math.cos(x2)*math.cos(y1-y2))))
stdio.writeln(d)
