import math

i = input().split()
print(i)
for n in i:
    n = float(n)/1000

    b = str(4*math.pi*(10**(-7))*5049.833887043189368770764120*n).replace('.', ',')
    print(b)

