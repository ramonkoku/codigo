vetor = [20, 15, 10, 30, 5]
produtos = ['veneno', 'espada', 'poção', 'arco', 'faca']
quantidade = [5, 3, 7, 2, 30]
preço = [5, 15, 25, 15, 2]

    
def adição(produtos, quantidade, preço):
    vetor.append(preço)
    vetor.append(produtos)
    vetor.append(quantidade)

def exibição_do_estoque():
    for i in range(len(produtos)):
        print(f"Produto: {produtos[i]}, Quantidade: {quantidade[i]}, Preço: {preço[i]}")

def venda(produto_index, quant_vendida):
    if quantidade[produto_index] >= quant_vendida:
        quantidade[produto_index] -= quant_vendida
    else:
        print(f"Não há estoque suficiente de {produtos[produto_index]} para vender {quant_vendida} unidades.")

venda (0, 3)
exibição_do_estoque()