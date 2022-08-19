N = int(input())
if 1 < N < 100:
    for i in range(1,N+1,):
        Q = i**2
        C = i**3
        print(i,Q,C)