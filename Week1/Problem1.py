def calculate_result():
    # Get two integers from the user
    num1 = int(input("Enter first integer: "))
    num2 = int(input("Enter second integer: "))

    # Calculate the product
    product = num1 * num2

    # Check the condition
    if product <= 5000:
        result = num1 + num2
        print(f"Product = {product} (<= 5000), so returning sum: {result}")
    else:
        result = product
        print(f"Product = {product} (> 5000), so returning product: {result}")

    return result

# Call the function
calculate_result()
