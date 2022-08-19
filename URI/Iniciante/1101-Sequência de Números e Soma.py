M,N = 1,1
while M > 0 and N > 0:
    x = input().split(' ')
    x = sorted(x)
    M = int(x[0])
    N = int(x[1])
    soma = 0
    if M > 0 and N > 0:
        for i in range(M,N+1):
            print(i,"",end="")
            soma = soma + i
        print("Sum=%d" %soma)