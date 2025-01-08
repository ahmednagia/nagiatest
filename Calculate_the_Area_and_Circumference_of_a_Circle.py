import math  # Import the math module to access the value of pi

# Get input from the user and convert it to a float
radius = float(input("Enter the radius of the circle: "))

# Calculate the area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area}")
print(f"Circumference of the circle: {circumference}")
