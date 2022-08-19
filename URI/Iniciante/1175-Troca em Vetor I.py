N=[]
cont=19
for i in range(20):
    N.append(int(input()))
for i in range(20):
    print("N[%d] = %d" %(i,N[cont]))
    cont -= 1