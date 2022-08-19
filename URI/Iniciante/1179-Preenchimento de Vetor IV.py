par = []
impar = []
contPar = 0
contImpar = 0

for i in range(15):
    n = int(input())

    if(n % 2 != 0):
        impar += [n]
        contImpar += 1

        if(contImpar == 5):

            for i in range(5):
                print("impar[%i] = %i" %(i,impar[i]))
            impar = []
            contImpar = 0

    if(n % 2 == 0):
        par += [n]
        contPar += 1

        if(contPar == 5):

            for i in range(5):
                print("par[%i] = %i" %(i,par[i]))
            par = []
            contPar = 0

for i in range(contImpar):
    print("impar[%i] = %i" %(i,impar[i]))

for i in range(contPar):
    print("par[%i] = %i" %(i,par[i]))