def findFactorial(number):
    if number<0:
        return -1
    if number == 0:
        return 1
    
    result=1

    for num in range(1,number+1):
        result=result*num

    return result

number=int(input("Enter the number : "))

factorial=findFactorial(number)

if factorial==-1:
    print("Factorial of a negative number is not possible")

else:
    print(f"Factorial of {number} is {factorial}")
    
