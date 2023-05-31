lista = ["Alexandre", "Alice", "André", "Arthur", "Arthur", "Artur", "Augusto", "Bernardo", "Bernardo", "Bruno",
         "Davi", "Diego", "Eduardo", "Fabrício", "Felipe", "Fernando", "Francisco", "Francisco", "Gabriel", "Gabriel",
         "Giovanna", "Giovanni", "Guilherme", "Guilherme", "Hector", "Henrique", "Inácio", "João", "João", "Joaquim",
         "Júlia", "Lauren", "Leonardo", "Leonardo", "Lucas", "Marina", "Matheus", "Matheus", "Paula", "Pedro", "Pedro",
         "Pedro", "Pedro", "Rafael", "Regis", "Sofia", "Stella", "Thiago", "Valentina", "Vicente", "Lucas"]

# Sor, tive dificuldade para fazer funcionar, devido alguns acentos
lista_ordenada = sorted(lista)


def obter_ultima_letra(nome):
    return nome[-1]

lista_ordenada_ultima_letra = sorted(lista, key=obter_ultima_letra)


print("Lista em ordem alfabética:")
for nome in lista_ordenada:
    print(nome)

print("\nLista ordenada pela última letra:")
for nome in lista_ordenada_ultima_letra:
    print(nome)