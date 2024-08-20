def transformar_int(valor):
    valor = (int) (valor)
    return valor

def validacaoInt(valor):
    try:
        valor = (int) (valor)
        return True
    except ValueError:
        print("Digite apenas inteiros!!!")
        return False

while True:
    dia = input("Digite o dia do seu nascimento: Ex: 1, 14, 21 \n")
    if validacaoInt(dia):
        dia = transformar_int(dia)
        break
    
while True:
    mes = input("Digite o mes do seu nascimento: Ex: 1, 14, 21 \n")
    if validacaoInt(mes):
        mes = transformar_int(mes)
        break
    
while True:
    ano = input("Digite o dia do seu nascimento: Ex: 1, 14, 21 \n")
    if validacaoInt(ano):
        ano = transformar_int(ano)
        break

match mes:
    case 1:
        mes = "Janeiro"
    case 2:
        mes = "Fevereiro"
    case 3:
        mes = "Março"
    case 4:
        mes = "Abril"
    case 5:
        mes = "Maio"
    case 6:
        mes = "Junho"
    case 7:
        mes = "Julho"
    case 8:
        mes = "Agosto"
    case 9:
        mes = "Setembro"
    case 10:
        mes = "Outubro"
    case 11:
        mes = "Novembro"
    case 12:
        mes = "Dezembro"

print(f"Você nasceu em {dia} de {mes} de {ano}")