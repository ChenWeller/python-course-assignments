import sys
import math

# Check that exactly one argument is provided (excluding the script name)
if len(sys.argv) != 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)

# Get radius from command line argument and convert to float
radius = float(sys.argv[1])

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print results
print("The area of the circle is:", round(area, 2))
print("The circumference of the circle is:", round(circumference, 2))

print("Thank you for using our circle program to compute your circle's area and circumference.")
