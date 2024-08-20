import random
from funcoes import gerarLista, imprimirLista, verificar_resultado, validacao_int, validacao_qnt_dezenas, validacao_numero_aposta
surpresinha1 = []
surpresinha2 = []
gabarito = []

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
            if validacao_numero_aposta(numero, aposta):
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

print(f"Quantidade de acertos da aposta: {verificar_resultado(aposta, gabarito)}")
print(f"Quantidade de acertos da surpresinha1: {verificar_resultado(surpresinha1, gabarito)}")
print(f"Quantidade de acertos da surpresinha2: {verificar_resultado(surpresinha2, gabarito)}")