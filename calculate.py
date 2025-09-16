#!/usr/bin/env python3

import sys
import math
from datetime import datetime

# Capture input arguments from the command line
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

# Step-by-step calculations
c_cubed = c ** 3                         # Step 1: c raised to the power of 3
sqrt_cubed = c_cubed ** 0.5              # Step 2: square root of c³
division = sqrt_cubed / a                # Step 3: divide the square root by a
multiplied = division * 10               # Step 4: multiply the result by 10
result = multiplied + b                  # Step 5: add b to the previous result

# Get current date and time
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Output formatted as HTML
print("Content-type: text/html\n")
print(f"{result:.1f}")
