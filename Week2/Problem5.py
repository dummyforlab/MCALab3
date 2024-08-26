def sumOfDigits(number):
    sum=0
    while number>0 :
        sum+=number%10
        number=number//10

    return sum

number=int(input("Enter the number : "))

sum=sumOfDigits(number)

print(f"Sum of digits of {number} is {sum}")
