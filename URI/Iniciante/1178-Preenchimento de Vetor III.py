X = float(input())
N=[]
N.append(X)
for i in range(100):
    if i == 0:
        print("N[%d] = %.4f" % (i, X))
    else:
        X = N[i-1] / 2
        N.append(X)
        print("N[%d] = %.4f" %(i,X))