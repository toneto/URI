N = int(input())
x = 1
for i in range(N):
    for j in range(4):
        if x % 4 != 0:
            print(x,end=" ")
        else:
            print("PUM")
        x+=1