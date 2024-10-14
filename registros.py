registros = []

# cria um loop infinito
while True:
    registros1= input("digite o 1 registo:")
    registros2= input("digite o 2 registo:")
    # registra o input do usuário
    if not registros1 or not registros2:
        if input("um dos registos esta vazio. sair ou escrevar"):
            print("registros salvo com sucesso:")
        else:
            break
    else:
        registros.extend([registros1, registros2])
        print("resgistros adicionados:",registros)            
    if registros:
        print("\n registro existentes:")
        for resgistro in registros:
            print(resgistro)