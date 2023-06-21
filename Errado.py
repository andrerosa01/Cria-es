# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

# Função para verificar se um jogador venceu
def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True
    
    # Verificar diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False

# Função para jogar
def jogar_jogo():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"
    
    while True:
        imprimir_tabuleiro(tabuleiro)
        linha = int(input("Digite o número da linha (0-2): "))
        coluna = int(input("Digite o número da coluna (0-2): "))
        
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            
            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print("Jogador", jogador_atual, "venceu!")
                break
            
            if jogador_atual == "X":
                jogador_atual = "O"
            else:
                jogador_atual = "X"
        else:
            print("Essa posição já está ocupada. Tente novamente.")

# Iniciar o jogo
jogar_jogo()