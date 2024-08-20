def solicitar_alternativa():
    while True:
        alternativa = input("Digite a alternativa correta (a, b, c, d, e): ").lower()
        if alternativa in ['a', 'b', 'c', 'd', 'e']:
            return alternativa
        else:
            print("Alternativa inválida. Por favor, digite novamente.")

def cadastrar_questao(questoes):
    enunciado = input("Digite o enunciado da questão:\n")
    alternativas = []
    letras = ['a', 'b', 'c', 'd', 'e']
    for letra in letras:
        alternativa = input(f"Digite a alternativa {letra}: ")
        alternativas.append(alternativa)
    resposta_correta = solicitar_alternativa()
    questoes.append({
        "enunciado": enunciado,
        "alternativas": alternativas,
        "resposta_correta": resposta_correta
    })
    print("Questão cadastrada com sucesso!")

def realizar_prova(questoes):
    letras = ['a', 'b', 'c', 'd', 'e']
    respostas_participante = []
    print("\nIniciando a prova...\n")
    for i, questao in enumerate(questoes):
        print(f"Questão {i+1}: {questao['enunciado']}")
        for j, alternativa in enumerate(questao['alternativas']):
            print(f"{letras[j]}) {alternativa}")
        resposta = solicitar_alternativa()
        respostas_participante.append(resposta)
    return respostas_participante

def calcular_resultado(questoes, respostas_participante):
    acertos = 0
    for i, questao in enumerate(questoes):
        if questao['resposta_correta'] == respostas_participante[i]:
            acertos += 1
    return acertos

def exibir_resultados(questoes, participantes):
    for participante, respostas in participantes.items():
        acertos = calcular_resultado(questoes, respostas)
        print(f"\nResultado de {participante}: {acertos}/{len(questoes)} acertos")

def main():
    questoes = []
    participantes = {}
    
    while True:
        print("\nEscolha uma opção:")
        print("1: Cadastrar questão objetiva")
        print("2: Realizar a prova")
        print("3: Exibir resultados")
        print("4: Sair")
        
        escolha = input("Digite o número da opção desejada: ").strip()
        
        if escolha == '1':
            cadastrar_questao(questoes)
        elif escolha == '2':
            if not questoes:
                print("Não há questões cadastradas.")
                continue
            nome_participante = input("Digite o nome do participante: ").strip()
            respostas_participante = realizar_prova(questoes)
            participantes[nome_participante] = respostas_participante
        elif escolha == '3':
            if not participantes:
                print("Nenhum participante realizou a prova ainda.")
                continue
            exibir_resultados(questoes, participantes)
        elif escolha == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()