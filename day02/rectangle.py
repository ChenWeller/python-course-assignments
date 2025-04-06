# Ask the user for height and width
height = input("Please enter the height of the rectangle, please be consistent with the units you choose: ")
width = input("Please enter the width of the rectangle, please be consistent with the units you choose: ")

# Convert the input strings to numbers - using float to acount for decimals
height = float(height)
width = float(width)

# Calculate the area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Print the results
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)
