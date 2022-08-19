X=[]
for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
        X.append(x)
    else:
        X.append(x)
    print("X[%d] = %d" % (i, x))