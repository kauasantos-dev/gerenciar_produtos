import gerenciar_arquivos

def exibir_produto(produto):
    for chave, valor in produto.items():
        if chave.lower() == 'produto':
            print(f"{chave}: {valor} |", end=" ")
        elif chave.lower() == 'preço':
            print(f"{chave}: R${valor:.2f} |", end=" ")
        elif chave.lower() == 'estoque':
            print(f"{chave}: {valor}\n")

def atualizar_atributo(lista_produtos):
    gerenciar_arquivos.AbrirArquivos.arquivo_w(lista_produtos)
    lista_produtos = gerenciar_arquivos.AbrirArquivos.arquivo_r()
    return lista_produtos