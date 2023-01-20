# prime number by taking range

def prime():    
    n=int(input("Enter last range: "))
    for i in range(1,n):
        prime=True   # Considering all numbers in the range are prime number
        if i==1:
            print(i,"is not prime and composite") # condition of value is 1
        for j in range(2,i):
            if i%j==0:
                prime=False  # Falsing the condition 
                break
            
        if prime:
            print(i,"is prime number")  # printing if prime number
        else:
            print(i,"is not prime number")  # printing if it is not prime number
prime()
