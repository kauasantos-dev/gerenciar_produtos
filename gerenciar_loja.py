import uteis
import gerenciar_arquivos 
from validadores import ValidarProduto

class Loja:
    def __init__(self):
        conteudo_arquivo = gerenciar_arquivos.AbrirArquivos.arquivo_r()
        self.__produtos = conteudo_arquivo if conteudo_arquivo else []
    
    @property
    def produtos(self):
        return self.__produtos
    
    def adicionar(self, nome, preco, estoque):
        try:
            nome = ValidarProduto.validar_nome(nome)
            if ValidarProduto.verificar_existencia_produto(nome, self.produtos):
                return False
            preco = ValidarProduto.validar_preco(preco)
            estoque = ValidarProduto.validar_estoque(estoque)
            novo_produto = {'Nome': nome, 'Preço': round(preco, 2), 'Estoque': estoque}
            self.__produtos.append(novo_produto)
            self.__produtos = uteis.atualizar_atributo(self.__produtos)
            return True
        except ValueError as erro:
            print(f"ERRO: {erro}\n")
            return False
    
    def listar_produtos(self):
        if self.produtos:
            print("PRODUTOS DA LOJA:\n")
            for produto in self.produtos:
                uteis.exibir_produto(produto)
            return True
        else:
            return False

    def buscar_produto(self, nome):
        if not ValidarProduto.verificar_existencia_produto(nome, self.produtos):
            return False
        print("PRODUTOS ENCONTRADOS:\n")
        for produto in self.produtos:
            if nome.lower() in produto['Nome'].lower():
                uteis.exibir_produto(produto)
            return True

    def excluir(self, nome):
        produto_encontrado = ValidarProduto.verificar_existencia_produto(nome, self.produtos)
        if produto_encontrado:
            self.__produtos.remove(produto_encontrado)
            self.__produtos = uteis.atualizar_atributo(self.__produtos)
            return True
        else:
            return False

    def atualizar_preco_estoque(self, nome_produto, preco_ou_estoque, opcao_selecionada, validador):
        if not ValidarProduto.verificar_existencia_produto(nome_produto, self.produtos):
            return False
        try:
            preco_ou_estoque = validador(preco_ou_estoque)
            produto_encontrado = ValidarProduto.verificar_existencia_produto(nome_produto, self.produtos)
            if opcao_selecionada == '5':
                produto_encontrado['Preço'] = preco_ou_estoque

            elif opcao_selecionada == '6':
                produto_encontrado['Estoque'] = preco_ou_estoque
            
            for i in range(len(self.__produtos)):
                if self.produtos[i]['Nome'].lower() == produto_encontrado['Nome'].lower():
                    self.__produtos[i] = produto_encontrado
                    break
            self.__produtos = uteis.atualizar_atributo(self.__produtos)
            return True
        except ValueError as erro:
            print(f"ERRO: {erro}\n")
            return None