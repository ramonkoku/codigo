filmes = ["Mundo de areia", "O Rei do inferno", "Raios gemeos"]

assentos = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

letras_fileiras = ["E", "D", "C", "B", "A"]

while True:
    print("\nFilmes em cartaz:")
    for i in range(len(filmes)):
        print(f"{i + 1}. {filmes[i]}")

    filme_escolhido = int(input("Escolha o número do filme (ou 0 para sair): ")) - 1
    if filme_escolhido == -1:  # Opção para sair do loop
        print("Encerrando o sistema de reservas. Obrigado!")
        break

    print("\nMapa de assentos:")
    print("  1 2 3 4 5")
    for i in range(len(assentos)):
        print(f"{letras_fileiras[i]} ", end="")
        print(" ".join(str(assento) for assento in assentos[i]))

    fileira_escolhida = input("\nEscolha a letra da fileira: ").upper()
    coluna_escolhida = int(input("Escolha o número da coluna: ")) - 1

    linha_escolhida = letras_fileiras.index(fileira_escolhida)

    if assentos[linha_escolhida][coluna_escolhida] == 0:
        assentos[linha_escolhida][coluna_escolhida] = 1
        print(f"\nAssento na fileira {fileira_escolhida}, coluna {coluna_escolhida + 1} reservado para o filme '{filmes[filme_escolhido]}'.")
    else:
        print("\nEsse assento já está ocupado!")

    print("\nMapa de assentos atualizado:")
    print("   1 2 3 4 5") 
    for i in range(len(assentos)):
        print(f"{letras_fileiras[i]} ", end="")
        print(" ".join(str(assento) for assento in assentos[i]))
