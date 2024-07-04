import random  # Importa o módulo random para gerar o número secreto

def jogar():
    imprime_mensagem_abertura()  # Chama a função para imprimir a mensagem de abertura do jogo

    def pede_numero():
        chute_str = input("Digite um número entre 1 e 100: ") 
        print("Você digitou ", chute_str)  # Imprime o número digitado pelo jogador
        return int(chute_str)  # Converte o número digitado para o tipo inteiro e o retorna

    def verifica_chute(chute, numero_secreto):
        pontos = 1000  # Define a pontuação inicial

        if chute == numero_secreto:  
            pontos_perdidos = (rodada - 1) * (pontos / total_de_tentativas)  
            pontuacao = pontos - pontos_perdidos  
            print("Você acertou e fez {} pontos!".format(pontuacao))  
            return True  # Retorna True para indicar que o jogador acertou
        else:
            if chute < numero_secreto:  
                pontos_perdidos = rodada * (pontos / total_de_tentativas)  
                print("Você errou! O seu chute foi menor do que o número secreto.")
                print("Você perdeu {} pontos".format(pontos_perdidos))  
                return False  # Retorna False para indicar que o jogador errou
            elif chute > numero_secreto:  
                pontos_perdidos = rodada * (pontos / total_de_tentativas)  
                print("Você errou! O seu chute foi maior do que o número secreto.")
                print("Você perdeu {} pontos".format(pontos_perdidos))  
                return False  # Retorna False para indicar que o jogador errou

    numero_secreto = random.randrange(1, 101)  # Gera um número aleatório entre 1 e 100 como número secreto
    total_de_tentativas = 0  # Inicializa o número total de tentativas

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))  

    if(nivel == 1):  # Define o número total de tentativas com base no nível de dificuldade escolhido
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):  
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute = pede_numero()  # Solicita ao jogador que faça um chute
        acertou = verifica_chute(chute, numero_secreto)  # Verifica se o chute do jogador está correto

        if acertou:
            break  

    print("Fim do jogo")
    print("O número secreto era: {}".format(numero_secreto))  

def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

if(__name__ == "__main__"):
    jogar()

