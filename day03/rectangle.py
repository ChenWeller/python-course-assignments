import sys

# Function to display the usage/help message
def show_help():
    print("Usage: python rectangle.py -h <height> -w <width>")
    print("Options:")
    print("  -h <height>   The height of the rectangle")
    print("  -w <width>    The width of the rectangle")
    print("  --help         Show this help message")

# Check if the user asked for help
if '--help' in sys.argv:
    show_help()
    sys.exit(0)

# Check if the correct number of arguments is provided (including the script name)
if len(sys.argv) != 5:
    print("Error: Invalid arguments.")
    show_help()
    sys.exit(1)

# Parse command-line arguments manually
height = None
width = None

for i in range(1, len(sys.argv), 2):
    if sys.argv[i] == '-h':
        height = float(sys.argv[i+1])
    elif sys.argv[i] == '-w':
        width = float(sys.argv[i+1])

# If height or width was not provided, display an error
if height is None or width is None:
    print("Error: Both height and width must be provided.")
    show_help()
    sys.exit(1)

# Calculate area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Print the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
