# Program to calculate the cube of all numbers from 1 to a given number

# Get input from the user
n = int(input("Enter the number: "))

# Calculate and display cubes
print(f"Cubes of numbers from 1 to {n}:")
for i in range(1, n + 1):
    print(f"{i}³ = {i**3}")
