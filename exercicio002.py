import random

surpresinha1 = []
surpresinha2 = []
gabarito = []

def gerarLista(lista, maxLista, minRange, maxRange):
    while len(lista) < maxLista:
        number = random.randint(minRange, maxRange)
        if number not in lista:
            lista.append(number)
    lista.sort()
    return lista

def imprimirLista(lista):
    print(", ".join(map(str, lista)))

def verificar_resultado(a_comparar):
    acertos = 0
    for i in range(len(a_comparar)):
        if a_comparar[i] in gabarito:
            acertos += 1
    return acertos

def validacao_int(valor):
    """
    Valida se o número é inteiro e retorna um aviso e False caso não seja.
    Caso seja inteiro, retorna a variável em formato inteiro e True.
    """
    try:
        valor = int(valor)
        return valor, True
    except ValueError:
        print("Digite apenas inteiros!!!")
        return None, False
    
def validacao_qnt_dezenas(valor):
    """
    Analisa a entrada do usuário e valida caso esteja dentro do intervalo válido
    """
    if valor in range(15, 19):  # Corrigi o range para incluir 18
        return True
    print("Valor fora do intervalo válido, digite novamente.")
    return False  # Retornar False caso o valor não seja válido
    
def validacao_numero_aposta(valor):
    if valor in aposta:
        print("Número repetido!")
        return False
    if valor not in dezenas_validas:
        print("Dezena Inválida")
        return False
    return True

while True:
    dezenas_desejadas = input("Digite quantas dezenas deseja marcar na primeira aposta: Entre 15 e 18\n")
    dezenas_desejadas, validacao = validacao_int(dezenas_desejadas)
    if validacao:
        if validacao_qnt_dezenas(dezenas_desejadas):
            break

aposta = []

dezenas_validas = list(range(1, 26))

for i in range(0, dezenas_desejadas):
    i += 1
    while True:
        numero = input(f"Digite o {i}º número da sua aposta: ")
        numero, validacao = validacao_int(numero)
        if validacao:
            if validacao_numero_aposta(numero):
                aposta.append(numero)
                break

surpresinha1 = gerarLista(surpresinha1, 18, 1, 25)
surpresinha2 = gerarLista(surpresinha2, 18, 1, 25)
gabarito = gerarLista(gabarito, 15, 1, 25)

print("Aposta:", end=" ")
imprimirLista(aposta)
print(f"Surpresinha 1:", end=" ")
imprimirLista(surpresinha1)
print(f"Surpresinha 2:", end=" ")
imprimirLista(surpresinha2)
print(f"Gabarito:", end=" ")
imprimirLista(gabarito)

print(f"Quantidade de acertos da aposta: {verificar_resultado(aposta)}")
print(f"Quantidade de acertos da surpresinha1: {verificar_resultado(surpresinha1)}")
print(f"Quantidade de acertos da surpresinha2: {verificar_resultado(surpresinha2)}")