def countDigits(number):
    count=0
    original=number
    while original>0 :
        original=original//10
        count+=1

    return count

number=int(input("Enter a number : "))
print(f"Total digits in {number} are {countDigits(number)}")
