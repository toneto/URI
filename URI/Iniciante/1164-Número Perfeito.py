N = int(input())
for i in range(N):
    soma=0
    X = int(input())
    for j in range(1, X):
        if X % j == 0:
            soma += j
    if (soma == X):
        print(X,"eh perfeito")
    else:
        print(X,"nao eh perfeito")