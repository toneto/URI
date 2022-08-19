N = int(input())
for i in range(N):
    n = input().split(" ")
    x = float(n[0])
    y = float(n[1])
    if y == 0:
        print("divisao impossivel")
    else:
        calc = x / y
        print("%.1f" % calc)