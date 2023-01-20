
#composite function

a=5
def comp(f,g):
    return lambda x:f(g(x))
def add(a):
    return a+5
def mul(a):
    return a*5
mul_add=comp(mul,add)
print(mul_add(a))





#composite function
a=5
def comp(f,g):
    return lambda x:f(g(x))
def sq(a):
    return a*a
def cu(a):
    return a*a*a
cu_sq=comp(cu,sq)
print(cu_sq(a))
