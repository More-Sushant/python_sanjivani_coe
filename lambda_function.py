#lambda function / anyonomus function

# simple code to deal with mathematical operations 


a=int(input("Enter Number "))   # taking first value from user
b=int(input("Enter Number "))   # taking second value from user

s=lambda x,y:x+y       # performing addition of that two number
                          # you can change operator and can perform different operations 

print(s(a,b))          # printing answer of above operation
