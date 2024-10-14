vetor = [20, 15, 10, 30, 5]
produtos = ['veneno', 'espada', 'poção', 'arco', 'faca']
quantidade = [5, 3, 7, 2, 30]
preço = [5, 15, 25, 15, 2]

# Função para atualizar o preço dos produtos
def atualização(novos_precos):
    global preço
    preço = novos_precos

# Função para adicionar um novo produto ao estoque
def adição(produto, quant, preco):
    produtos.append(produto)
    quantidade.append(quant)
    vetor.append(preco)

# Função para exibir o estoque atual
def exibição_do_estoque():
    for i in range(len(produtos)):
        print(f"Produto: {produtos[i]}, Quantidade: {quantidade[i]}, Preço: {vetor[i]}")

# Função para vender produtos
def venda(produto_index, quant_vendida):
    if quantidade[produto_index] >= quant_vendida:
        quantidade[produto_index] -= quant_vendida
    else:
        print(f"Não há estoque suficiente de {produtos[produto_index]} para vender {quant_vendida} unidades.")

# Atualizando o estoque com as vendas
venda(0, 3)  # Vendendo 3 unidades do produto 1 (veneno)
venda(3, 2)  # Vendendo 2 unidades do produto 4 (arco)

# Adicionando 10 unidades ao produto 5 (faca)
quantidade[4] += 10

# Exibindo o estoque atualizado
exibição_do_estoque()
