import config_arquivos
import json

class Produtos:
    def __init__(self):
        self.__lista = []

    def adicionar(self, nome, preco, estoque):
        nome = self.validar_nome(nome)
        preco = self.validar_preco(preco)
        estoque = self.validar_estoque(estoque)
        self.produto = {'Produto': nome, 'Preço': round(preco, 2), 'Estoque': estoque} 
        try:
            with open(config_arquivos.save_to, "x", encoding="utf-8") as file:
                self.__lista.append(self.produto)
                json.dump(self.__lista, file, indent=2, ensure_ascii=False)
        except FileExistsError:          
            self.__lista = self.arquivo_r()
            self.__lista.append(self.produto)
            self.arquivo_w(self.__lista)
        print("\nProduto adicionado com sucesso!\n")
    
    def listar_produtos(self):
        try:
            self.__lista = self.arquivo_r()
            if not self.__lista:
                print("Erro: Não há produtos cadastrados.\n")
                return
            else:
                  print("\nProdutos cadastrados:\n")
                  for produto in self.__lista:
                      for chave, valor in produto.items():
                          if chave.lower() == 'produto':
                              print(f"{chave}: {valor} |", end=" ")
                          elif chave.lower() == 'preço':
                              print(f"{chave}: R${valor:.2f} |", end=" ")
                          elif chave.lower() == 'estoque':
                              print(f"{chave}: {valor}")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def buscar(self, nome):
        nome = self.validar_nome(nome)
        try:
            self.__lista = self.arquivo_r()
            verificar = False
            for i in range(len(self.__lista)):
                if nome.lower() == self.__lista[i]['Produto'].lower():
                    verificar = True
                    produto = self.__lista[i]
            if verificar:
               print("Produto encontrado:\n")
               for chave, valor in produto.items():
                  if chave.lower() == 'produto':
                     print(f"{chave}: {valor} |", end=" ")
                  elif chave.lower() == 'preço':
                     print(f"{chave}: R${valor:.2f} |", end=" ")
                  elif chave.lower() == 'estoque':
                     print(f"{chave}: {valor}")
                     return
            else:
                print("\nNenhum produto encontrado.\n")
                return
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")

    def excluir(self, nome):
        nome = self.validar_nome(nome)
        try:
            self.__lista = self.arquivo_r()
            verificar = False
            for i in range(len(self.__lista)):
                if nome.lower() == self.__lista[i]['Produto'].lower():
                    verificar = True
                    indice = i
                    break
            if verificar:
                del self.__lista[indice]
            else:
                print("\nNenhum produto encontrado.\n")
                return
            self.arquivo_w(self.__lista)
            print("\nProduto excluído com sucesso!\n")
        except FileNotFoundError:
            print("Erro: Não há produtos cadastrados.\n")     

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
    
    def arquivo_r(self):
        with open(config_arquivos.save_to, "r", encoding="utf-8") as file:
            return json.load(file)
    
    def arquivo_w(self, lista):
        with open(config_arquivos.save_to, "w", encoding="utf-8") as file:
            json.dump(lista, file, indent=2, ensure_ascii=False)