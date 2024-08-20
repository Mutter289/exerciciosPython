import random

def gerarLista(lista, maxLista, minRange, maxRange):
    while len(lista) < maxLista:
        number = random.randint(minRange, maxRange)
        if number not in lista:
            lista.append(number)
    lista.sort()
    return lista

def imprimirLista(lista):
    print(", ".join(map(str, lista)))

def verificar_resultado(a_comparar, gabarito):
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
    
def validacao_numero_aposta(numero, aposta):
    if numero in aposta:
        print("Número repetido!")
        return False
    if numero not in list(range(1, 26)):
        print("Dezena Inválida")
        return False
    return True