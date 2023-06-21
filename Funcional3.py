import random

def jogo_pedra_papel_tesoura():
    escolhas = ["Pedra", "Papel", "Tesoura"]
    escolha_usuario = input("Escolha: Pedra, Papel ou Tesoura? ").capitalize()

    if escolha_usuario in escolhas:      #Agora rescrito, a parte da escolha, é possivel iniciar o jogo sem problemas
        escolha_computador = random.choice(escolhas)

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