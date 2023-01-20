#scope of variable

a=100   # a is golbal variable 

def xyz():
    a=10    # here a is acting as local variable
    print(a)    # printing a as local variable
    
print(a)    # printing a as global variable 

xyz()     # calling of function named as xyz
