def isPrime(n):
    if n<=1:
        return False
    if n<=3:
        return True
    if n%2==0 or n%3==0:
        return False
    
    i=5

    while i*i<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6

    return True

start=int(input("Enter start : "))
end=int(input("Enter end : "))

primes=[]

for num in range(start,end+1):
    if(isPrime(num)):
        primes.append(num)

print(f"Primes b/w {start} and {end} are {primes}")
