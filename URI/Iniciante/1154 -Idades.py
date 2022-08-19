li=[]
idade = 2
x = 0
while idade >= 0:
    idade = float(input())
    if idade >= 0:
        li.append(idade)
        x+=1
media = (sum(li))/x
print("%.2f"%media)