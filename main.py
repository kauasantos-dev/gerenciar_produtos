import sys

import uteis
import validadores
import gerenciar_loja

if __name__ == '__main__':

  loja = gerenciar_loja.Loja()
  print("===== GERENCIAMENTO DE PRODUTOS =====\n")
  while True:
    uteis.menu_opcoes()
    opcao = input()

    if opcao == '1':
      loja.listar_produtos()
        
    elif opcao == '2':
      nome = input("Digite o nome do produto: ")
      preco = input("Informe o preço do produto: ")
      estoque = input("Informe o estoque do produto: ")
      if loja.adicionar(nome, preco, estoque):
        print("PRODUTO ADICIONADO COM SUCESSO!\n")
      
    elif opcao == '3':
      if not loja.buscar_produto(input("Digite o nome do produto: ")):
        print("PRODUTO NÃO ENCONTRADO.\n")

    elif opcao == '4':
      if loja.excluir(input("Informe o nome do produto: ")):
        print("PRODUTO REMOVIDO COM SUCESSO!\n")
      else:
        print("PRODUTO NÃO ENCONTRADO.\n")

    elif opcao == '5':
      while True:
        try:
          nome = input("Informe o nome do produto: ")
          preco = input("Informe o novo preço do produto: ")
          loja.atualizar(nome, preco, opcao)
          break
        except ValueError as e:
          print("Erro: ", e, " Tente novamente.\n")


    elif opcao == '6':
      while True:
        try:
          nome = input("Digite o nome do produto: ")
          estoque = input("Informe o novo estoque do produto: ")
          loja.atualizar(nome, estoque, opcao)
          break
        except ValueError as e:
          print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '7':
      print("\nPrograma encerrado.")
      sys.exit(0)

    else:
      print("\nOpção inválida. Por favor, digite uma opção válida.\n")