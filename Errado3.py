import random

def jogo_pedra_papel_tesoura():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    escolha_usuario = input("Escolha: Pedra, Papel ou Tesoura? ").capitalize() #o problema ocorre quando o usuário faz uma escolha inválida, ou seja, uma escolha que não seja "Pedra", "Papel" ou "Tesoura".
    escolha_computador = random.choice(escolhas) #isso faz causar erro, e nao funciona

    if escolha_usuario == "Pedra":
        if escolha_computador == "Papel":
            print("Você perdeu! Papel vence Pedra.")
        elif escolha_computador == "Tesoura":
            print("Você ganhou! Pedra vence Tesoura.")
        else:
            print("Empate!")
    elif escolha_usuario == "Papel":
        if escolha_computador == "Pedra":
            print("Você ganhou! Papel vence Pedra.")
        elif escolha_computador == "Tesoura":
            print("Você perdeu! Tesoura vence Papel.")
        else:
            print("Empate!")
    elif escolha_usuario == "Tesoura":
        if escolha_computador == "Pedra":
            print("Você perdeu! Pedra vence Tesoura.")
        elif escolha_computador == "Papel":
            print("Você ganhou! Tesoura vence Papel.")
        else:
            print("Empate!")
    else:
        print("Escolha inválida. Tente novamente.")

jogo_pedra_papel_tesoura()