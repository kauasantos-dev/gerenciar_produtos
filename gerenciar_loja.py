import json

import uteis
import caminho_arquivos
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
        nome = ValidarProduto.validar_nome(nome)
        if ValidarProduto.verificar_existencia_produto(nome, self.produtos):
            return False
        preco = ValidarProduto.validar_preco(preco)
        estoque = ValidarProduto.validar_estoque(estoque)
        novo_produto = {'Produto': nome, 'Preço': round(preco, 2), 'Estoque': estoque}
        self.__produtos.append(novo_produto)
        gerenciar_arquivos.AbrirArquivos.arquivo_w(self.__produtos)
        self.__produtos = gerenciar_arquivos.AbrirArquivos.arquivo_r()
        return True
    
    def listar_produtos(self):
        if self.__produtos:
            print("PRODUTOS DA LOJA:\n")
            for produto in self.__produtos:
                uteis.exibir_produto(produto)
        else:
            return False

    def buscar_produto(self, nome):
        if not ValidarProduto.verificar_existencia_produto(nome, self.__produtos):
            return False
        print("PRODUTOS ENCONTRADOS:\n")
        for produto in self.__produtos:
            if nome.lower() in produto['Nome'].lower():
                uteis.exibir_produto(produto)

    def excluir(self, nome):
        produto_encontrado = None
        if not self.__produtos:
            return False
        else:
            for produto_salvo in self.__produtos:
                if nome.lower() == produto_salvo['Nome'].lower():
                    produto_encontrado = produto_salvo
                    break
            if produto_encontrado:
                self.__produtos.remove(produto_encontrado)
                gerenciar_arquivos.AbrirArquivos.arquivo_w(self.__produtos)
                self.__produtos = gerenciar_arquivos.AbrirArquivos.arquivo_r()
                return True
            else:
                return None

    def atualizar_preco_estoque(self, nome_produto, preco_ou_estoque, opcao_selecionada, validador):
        if not self.__produtos or not ValidarProduto.verificar_existencia_produto(nome_produto, self.__produtos):
            return False
        try:
            preco_ou_estoque = validador(preco_ou_estoque)
            produto_encontrado = ValidarProduto.verificar_existencia_produto(nome_produto, self.__produtos)
            if opcao_selecionada == '5':
                produto_encontrado['Preço'] = preco_ou_estoque

            elif opcao_selecionada == '6':
                produto_encontrado['Estoque'] = preco_ou_estoque
            
            for i in range(len(self.__produtos)):
                if self.__produtos[i]['Nome'].lower() == produto_encontrado['Nome'].lower():
                    self.__produtos[i] = produto_encontrado
                    break

            gerenciar_arquivos.AbrirArquivos.arquivo_w(self.__produtos)
            self.__produtos = gerenciar_arquivos.AbrirArquivos.arquivo_r()
            return True
        except ValueError as erro:
            print(f"ERRO: {erro}.\n")