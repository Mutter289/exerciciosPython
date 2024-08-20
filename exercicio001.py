def calculo_pagar(dias, km):
    """
    Calcula quanto o cliente irá pagar
    """
    dias = int(dias)
    km = int(km)
    pagar = (dias * 70) + (km * 0.10)
    return pagar

clientes = {}
total_km = 0
total_clientes = 0

while True:
    nome = input("Digite seu nome (ou SAIR para encerrar): ")
    if nome.upper() == "SAIR":
        break

    sexo = input("Digite seu sexo: F para feminino, M para masculino\n").upper()
    while sexo not in ['F', 'M']:
        sexo = input("Sexo inválido. Digite F para feminino, M para masculino\n").upper()

    placa = input("Digite a placa do carro: ")
    km_contratados = input("Digite os km contratados: ")
    while not km_contratados.isdigit():
        km_contratados = input("Valor inválido. Digite os km contratados: ")
    
    dias_contratados = input("Digite a quantidade de dias contratados: ")
    while not dias_contratados.isdigit():
        dias_contratados = input("Valor inválido. Digite a quantidade de dias contratados: ")

    total_pagar = calculo_pagar(dias_contratados, km_contratados)
    
    cliente = {
        "nome": nome,
        "sexo": "Feminino" if sexo == "F" else "Masculino",
        "placa": placa,
        "km_contratados": int(km_contratados),
        "dias_contratados": int(dias_contratados),
        "total_pagar": total_pagar
    }

    clientes.update(cliente)
    total_km += cliente["km_contratados"]
    total_clientes += 1

    print(f"Placa do carro: {cliente['placa']}, Valor total a pagar: R$ {cliente['total_pagar']:.2f}")
    print(clientes)

# Calcular e imprimir a média de quilômetros contratados pelos clientes
if total_clientes > 0:
    media_km = total_km / total_clientes
    print(f"Média de quilômetros contratados: {media_km:.2f}")

    # Calcular e imprimir o nome das clientes de sexo feminino que fecharam aluguéis acima de 7 dias contratados
    print("Clientes do sexo feminino que fecharam aluguéis acima de 7 dias contratados:")
    for cliente in clientes:
        if cliente["sexo"] == "Feminino" and cliente["dias_contratados"] > 7:
            print(cliente["nome"])
else:
    print("Nenhum cliente registrado.")