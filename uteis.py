def exibir_produto(produto):
    for chave, valor in produto.items():
        if chave.lower() == 'produto':
            print(f"{chave}: {valor} |", end=" ")
        elif chave.lower() == 'preço':
            print(f"{chave}: R${valor:.2f} |", end=" ")
        elif chave.lower() == 'estoque':
            print(f"{chave}: {valor}\n")