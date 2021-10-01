from math import factorial
def cds():
    n=int(input("donner n: "))
    while (n<2 or n>10):
        n=int(input("donner n: "))
    return n
def construire(n):
    for i in range(n):
        for j in range(n-i+1): 
            print(end="\n") 
        for j in range(i+1):
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=" ")
#pp
n=cds()
construire(n)
