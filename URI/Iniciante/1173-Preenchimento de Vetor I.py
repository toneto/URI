V = int(input())
N=[]
N.append(V)
for i in range(10):
    if i == 0:
        print("N[%d] = %d" % (i, V))
    else:
        X = 2 * N[i-1]
        N.append(X)
        print("N[%d] = %d" %(i,X))