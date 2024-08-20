import funcoes

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
            funcoes.cadastrar_questao(questoes)
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