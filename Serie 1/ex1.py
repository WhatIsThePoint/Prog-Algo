import random
def cds():
    n=int(input("donner la taille de la matrice: "))
    while (n<2):
        n=int(intput("donner la taille de la matrice: "))
    return n
def remplir(m,n):
    for i in range (n):
        for j in range (n):
            x=random.randint(0,1)
            print(x)
            m[i][j]=x
def verif(m,n):
    for i in range (n):
        for j in range (n):
            if (m[i][i]==1):
                v=True
            else:
                v=False
                break
        if (v==False):
            break
    if (v==True):
        print("identique")
    else:
        print("non identique")
    
        
#pp
n=cds()
m=[["" for i in range(n)]for j in range(n)]
print (m)
remplir(m,n)
print(m)
verif(m,n)
