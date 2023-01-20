

#scope of variable

a=15    # golbal variable 
def cir():
    a=10    #local variable
    def sq():
        print(a*a)    # printing square of a with updated value if sq() function is called 
    def cu():
        nonlocal a    # creating non local variable
        a=5
        print(a*a*a)  # printing cube of a with updated value if cu() function is called
    sq()
    cu()
print("Global value of a is",a) #printing global value of a 
cir()
