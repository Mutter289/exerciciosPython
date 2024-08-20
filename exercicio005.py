import random

num_sorteados = []
    
def sortear(numInicio, numFinal, qtdNumero):
    while len(num_sorteados) < qtdNumero:
        num = random.randint(numInicio, numFinal)
        if num not in num_sorteados:
            num_sorteados.append(num)
        else:
            continue
    num_sorteados.sort()

sortear(1,60,6)

print("Sorteio da Mega Sena:")

c = 0
for i in num_sorteados:
    c += 1
    if c == len(num_sorteados):
        print(i)
    else:
        print(i, end=", ")
