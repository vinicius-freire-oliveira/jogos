import random #permite gerar números aleatórios

# será chamada para iniciar o jogo da forca, esta é a função principal
# executa a lógica do jogo dentro de um laço while
def jogar():
    imprime_mensagem_abertura()  # Chama a função para imprimir a mensagem de abertura do jogo
    palavra_secreta = carrega_palavra_secreta()  # Carrega uma palavra secreta do arquivo

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)  # Inicializa a lista de letras acertadas
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0
    letras_erradas = []  # Lista para armazenar as letras incorretas

    while(not enforcou and not acertou):
        chute = pede_chute()  # Solicita ao jogador que informe uma letra para o chute

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)  # Marca as letras corretas no jogo da forca
        else:
            erros += 1
            letras_erradas.append(chute)  # Adiciona a letra incorreta à lista de letras erradas
            desenha_forca(erros)  # Desenha a parte correspondente da figura da forca

        enforcou = erros == 7  # Verifica se o número de erros é igual a 7 (o jogador perdeu)
        acertou = "_" not in letras_acertadas  # Verifica se todas as letras foram acertadas

        print(letras_acertadas)
        print("Letras erradas: {}".format(letras_erradas))

    if(acertou):
        imprime_mensagem_vencedor()  
    else:
        imprime_mensagem_perdedor(palavra_secreta)  

# Essa função imprime uma mensagem de abertura para o jogo da forca
def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

# Carrega uma palavra secreta do arquivo "palavras.txt". O arquivo contém uma lista de palavras, cada uma em uma linha.
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")  # Abre o arquivo "palavras.txt" no modo de leitura ("r") e atribuímos o objeto de arquivo retornado à variável arquivo
    palavras = []

    for linha in arquivo:
        linha = linha.strip()  # Remove espaços em branco no início e no final da linha
        palavras.append(linha)

    arquivo.close()  # Após ler todas as linhas do arquivo, fechamos o arquivo para liberar os recursos do sistema

    numero = random.randrange(0, len(palavras))  # Esse número aleatório será usado como um índice para selecionar uma palavra aleatória da lista palavras
    palavra_secreta = palavras[numero].upper()  # Seleciona a palavra aleatória e a converte para letras maiúsculas. A palavra secreta selecionada é armazenada na variável palavra_secreta
    return palavra_secreta # retornamos a palavra secreta selecionada para ser usada no jogo

# Inicializa a lista de letras acertadas com "_" para cada letra da palavra secreta
# Recebe a palavra secreta como argumento e retorna uma lista contendo "". Cada "" representa uma letra a ser adivinhada pelo jogador
# Essa lista será usada para rastrear as letras que o jogador já adivinhou corretamente e para exibir o progresso do jogo
def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]  # Cria uma lista com "_" para cada letra da palavra secreta. Construção para criar listas de forma compacta.

# Solicita ao jogador que informe uma letra para o chute e retorna o valor fornecido
def pede_chute():
    chute = input("Qual letra? ")  
    chute = chute.strip().upper()  
    return chute

# Marca as letras corretas no jogo da forca. Ela recebe o chute do jogador, a lista de letras acertadas e a palavra secreta
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0 # será usada para rastrear a posição atual na palavra secreta
    for letra in palavra_secreta: # percorremos cada letra da palavra secreta usando um loop for
        if (chute == letra): 
            letras_acertadas[index] = letra  # Atualiza a lista de letras acertadas com a letra correta. 
        index += 1 # incrementamos o valor de index em 1 para avançar para a próxima posição na lista de letras acertadas e na palavra secreta

# Recebe o número de erros e imprime a parte correspondente da figura da forca, dependendo do número de erros
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(erros == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(erros == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(erros == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(erros == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(erros == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (erros == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

# Imprime uma mensagem de parabéns quando o jogador vence o jogo
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

# Imprime uma mensagem de derrota quando o jogador perde o jogo, juntamente com a palavra secreta
def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

# Condição de execução principal
# Essa condição verifica se o módulo está sendo executado como programa principal e, em seguida, chama a função jogar() para iniciar o jogo da forca.
if(__name__ == "__main__"):
    jogar()