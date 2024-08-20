import string

def obter_palavra_secreta():
    """Solicita ao usuário para digitar uma palavra secreta e retorna a palavra em minúsculas."""
    palavra = input("Digite a palavra secreta: ").strip().lower()
    while not palavra.isalpha():
        print("A palavra deve conter apenas letras.")
        palavra = input("Digite a palavra secreta: ").strip().lower()
    return palavra

def exibir_progresso(palavra_secreta, letras_corretas):
    """Exibe o progresso atual do jogo, mostrando as letras acertadas e os espaços em branco para as letras não acertadas."""
    progresso = [letra if letra in letras_corretas else '_' for letra in palavra_secreta]
    print(" ".join(progresso))

def jogar_forca():
    """Função principal para jogar o jogo da forca."""
    palavra_secreta = obter_palavra_secreta()
    letras_corretas = set()
    letras_erradas = set()
    tentativas_restantes = 3
    
    print("\nComece a jogar!")
    
    while tentativas_restantes > 0:
        exibir_progresso(palavra_secreta, letras_corretas)
        print(f"Tentativas restantes: {tentativas_restantes}")
        
        palpite = input("Digite uma letra: ").strip().lower()
        
        if len(palpite) != 1 or not palpite.isalpha():
            print("Por favor, digite uma única letra.")
            continue
        
        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if palpite in palavra_secreta:
            letras_corretas.add(palpite)
            print("Bom trabalho! Letra correta.")
        else:
            letras_erradas.add(palpite)
            tentativas_restantes -= 1
            print("Letra incorreta.")
        
        if all(letra in letras_corretas for letra in palavra_secreta):
            print(f"\nParabéns! Você adivinhou a palavra: {palavra_secreta}")
            break
    else:
        print(f"\nVocê perdeu! A palavra secreta era: {palavra_secreta}")

def main():
    """Função principal para executar o jogo da forca."""
    jogar_forca()

if __name__ == "__main__":
    main()
