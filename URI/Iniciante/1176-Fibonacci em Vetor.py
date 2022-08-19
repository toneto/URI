fib=[]
fib.append(0)
fib.append(1)
for i in range(64 - 2):
    x = fib[i] + fib[i + 1]
    fib.append(x)
T = int(input())
for j in range(T):
    N = int(input())
    print('Fib(%d) = %d' % (N, fib[N]))