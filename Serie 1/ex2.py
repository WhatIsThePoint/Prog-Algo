import random
def cds():
    n=int(input("donner la taille de la matrice: "))
    while (n<0):
        n=int(intput("donner la taille de la matrice: "))
    return n
def remplir(m,n):
    for i in range (n):
        for j in range (n):
            x=random.randint(3,8)
            m[i][j]=x
    print(m)
def verif(m,n):
    s1=0
    s2=0
    for i in range (n):
        for j in range (n):
            if (i==j):
                s1+=m[i][j]
            if (i==n-j-1):
                s2+=m[i][j]
    print (s1,s2)
    if (s1==s2):
        print("c'est magique!!!")
    else:
        print("c'est pas magique :(")
#pp
n=cds()
m=[["" for i in range(n)]for j in range(n)]
print (m)
remplir(m,n)
verif(m,n)

