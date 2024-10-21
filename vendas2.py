vendas = [120, 130, 140, 150, 160, 170, 160, 150, 140, 130, 120, 110]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

matriz_vendas = [[meses[i], vendas[i]] for i in range(len(vendas))]

for mes, venda in matriz_vendas:
    print(f"{mes}: {venda} vendas")


total_vendas = sum(vendas)

media_mensal = total_vendas / len(vendas)


max_venda = max(vendas)
mes_max_venda = vendas.index(max_venda) + 1  

print("\n")
print(f"Total de vendas no ano: {total_vendas}")
print(f"Média mensal de vendas: {media_mensal:.2f}")
print(f"Mês com a máxima venda: {mes_max_venda} (vendas: {max_venda})")
