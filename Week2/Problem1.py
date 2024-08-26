def digitsReverse(number):
    original=number
    print()
    print("The digits in reverse order are : ")
    while original>0:
        print(original%10)
        original=original//10


number=int(input("Enter a number : "))

digitsReverse(number)
