u1=[]
L=[]
u2=[]
for i in range(5):
    n=int(input("entrer un nombre: "))
    u1.append(n)
for i in range(5):
    while True:
        N=int(input("entrer soit une valeur de 1 ou 0: "))
        if N==0 or N==1:
            L.append(N)
            break
for i in range(5):
    if L[i]==1:
        u2[i]= u1[i]
    if L[i]==0:
        u2[i]= u1[i+1]
        break
print("u1:",u1)
print("L:",L)
print("u2:",u2)
