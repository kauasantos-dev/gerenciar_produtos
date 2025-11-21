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

    def atualizar(self, nome, numero, opcao):
        nome = self.validar_nome(nome)
        if opcao == '5':
          numero = self.validar_preco(numero)
        elif opcao == '6':
            numero = self.validar_estoque(numero)
        try:
              self.__lista = self.arquivo_r()
              verificar = False
              for i in range(len(self.__lista)):
                  if nome.lower() == self.__lista[i]['Produto'].lower():
                     verificar = True
                  if opcao == '5' and verificar:
                         self.__lista[i]['Preço'] = round(numero, 2)
                         print("\nPreço atualizado com sucesso!\n")
                         break
                  elif opcao == '6' and verificar:
                         self.__lista[i]['Estoque'] = numero
                         print("Estoque atualizado com sucesso!\n")
                         break
              if not verificar:
                  print("\nNenhum produto encontrado.\n")
                  return
              self.arquivo_w(self.__lista)
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")