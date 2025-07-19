# Program to check if a number is a palindrome

# Take input from the user
number = int(input("Enter a number: "))

# Convert number to string for easy reversal
original_str = str(number)
reversed_str = original_str[::-1]

# Check for palindrome
if original_str == reversed_str:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
