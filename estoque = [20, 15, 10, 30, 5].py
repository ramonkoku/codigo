estoque = [20, 15, 10, 30, 5]

# Função para adicionar um item ao estoque
def adicionar_item(item):
    estoque.append(item)
    print(f"Item {item} adicionado ao estoque.")

# Função para atualizar a quantidade de um item no estoque
def atualizar_item(index, nova_quantidade):
    if index < len(estoque):
        estoque[index] = nova_quantidade
        print(f"Quantidade do item na posição {index} atualizada para {nova_quantidade}.")
    else:
        print(f"Índice {index} fora do intervalo do estoque.")

# Função para exibir o estoque
def exibir_estoque():
    for i, quantidade in enumerate(estoque):
        print(f"Índice: {i}, Quantidade: {quantidade}")

# Exemplo de uso das funções
adicionar_item(25)
atualizar_item(4, 45)
exibir_estoque()