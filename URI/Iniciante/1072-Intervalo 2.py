n = int(input())
dentro = 0
fora = 0
x=[]

for i in range (n):
    x.append(input())

for i in x:
    if (10 <= int(i) <= 20):
        dentro += 1
    elif (int(i) > 20) or(int(i) < 10):
        fora += 1

print(dentro, "in")
print(fora, "out")