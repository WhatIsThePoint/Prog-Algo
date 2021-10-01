import random
def cds():
    n=int(input("donner la taille de la matrice: "))
    while (n<4 or n>20):
        n=int(input("donner la taille de la matrice: "))
    return n
def remplir(m,n):
    for i in range (n):
        for j in range (n):
            x=random.randint(2,99)
            while(premier(x)):
                 x=random.randint(2,99)
            m[i][j]=x
    print(m)
def premier(x):
    v=False
    for i in range(2, x):
        if (x % i) == 0:
            v = True
            break
    return v
       
def verif(m,n):
    for i in range (n):
        print (m[i])
#pp
n=cds()
m=[["" for i in range(n)]for j in range(n)]
print (m)
remplir(m,n)
verif(m,n)
