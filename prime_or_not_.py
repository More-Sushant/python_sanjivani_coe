#prime number by taking single value
def prime():
    n=int(input("Enter Number"))
    prime=True  # considering all numbers are prime
    c=2
    while n>c:
        if n%c==0:
            prime=False   # Changing the value if number are not prime 
            break
        c=c+1
    if prime:
        print(n,"is prime number")   # prining if number is prime 
    else:
        print(n,"is not prime number")   # prime if number is not prime
prime()
