s=float(input())
if (0<s<=400):
    rea=(((s*15)/100)+s)
    perc= 15
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-s))
    print("Em percentual: " + str(perc) + " %")
elif(400<s<=800):
    rea=(((s*12)/100)+s)
    perc= 12
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-s))
    print("Em percentual: " + str(perc) + " %")
elif(800<s<=1200):
    rea=(((s*10)/100)+s)
    perc= 10
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-s))
    print("Em percentual: " + str(perc) + " %")
elif(1200<s<=2000):
    rea=(((s*7)/100)+s)
    perc= 7
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-s))
    print("Em percentual: " + str(perc) + " %")
else:
    rea=(((s*4)/100)+s)
    perc= 4
    print("Novo salario: %.2f" %rea)
    print("Reajuste ganho: %.2f" %(rea-s))
    print("Em percentual: " + str(perc) + " %")