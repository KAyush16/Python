# def fact(n):
#     """ calculate n! interatively
#     """
#     result=1
#     if n>1:
#         for f in range(2,n+1):
#             result*=f
#     return result# this will also return if n<1 then it will directly to 1
    
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)
    
def fibb(n):
    """ F(n)= F(n-1)+ F(n-2) """
    if n<2:
        return n
    else:
        return fibb(n-1)+fibb(n-2)
for i in range(12):
    print(i,factorial(i))
