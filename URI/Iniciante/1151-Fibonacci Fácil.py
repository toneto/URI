Q = int(input())
r=[]
r.append(0)
r.append(1)
for i in range(Q - 2):
    x = r[i] + r[i+1]
    r.append(x)

print(r[0],end="")
for i in range(1,Q):
    print("",r[i],end="")
print()