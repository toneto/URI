T=int(input())
N=[]
x=0
for i in range(1000):
    N.append(x)
    print("N[%d] = %d" %(i,x))
    if x < T-1:
        x = x + 1
    elif x == T-1:
        x = 0