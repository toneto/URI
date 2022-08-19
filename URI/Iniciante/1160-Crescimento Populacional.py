T = int(input())
while T > 0:
    PA, PB, G1, G2 = map(float, input().split())
    anos = 0
    while PA <= PB:
        PA += int(PA * (G1 / 100))
        PB += int(PB * (G2 / 100))
        anos += 1
        if anos > 100:
            print("Mais de 1 seculo.")
            break

    if anos <= 100: print("%d anos." % anos)
    T -= 1