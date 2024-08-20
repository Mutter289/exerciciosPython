def validacaoInt(valor):
    try:
        valor = (int) (valor)
        return True
    except ValueError:
        return False

def converterInt(valor):
    valor = (int) (valor)
    return valor

def imprimirHorario(hora, minuto):
    horario = [hora, minuto]
    if hora > 12:
        horario[0] = hora - 12
        print(":".join(map(str, horario)), end=" PM")
    else:
        print(":".join(map(str, horario)), end=" AM")

def main():
    while True:
        hora = input("Digite a hora: Ex: 9, 12, 17 \n")
        if validacaoInt(hora):
            hora = converterInt(hora)
            break
    while True:
        minuto = input("Digite os minutos: Ex: 24, 47, 39 \n")
        if validacaoInt(minuto):
            minuto = converterInt(minuto)
            break
    imprimirHorario(hora, minuto)

if __name__ == "__main__":
    main()