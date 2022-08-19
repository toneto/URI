N = int(input())
if 1 < N < 1000:
    for i in range(1,N+1,):
        Q = i**2
        C = i**3
        print(i,Q,C)
        print(i,Q+1,C+1)