import sys

import gerenciar_loja

if __name__ == '__main__':
  
  loja = gerenciar_loja.Loja()
  print("===== GERENCIAMENTO DE PRODUTOS =====\n")
  while True:
    print("\nSelecione uma opção abaixo (digite o número da opção):\n")
    print("[1]- Ver produtos cadastrados\n[2]- Adicionar novo produto\n[3]- Buscar produto\n[4]- Excluir produto\n[5]- Atualizar preço\n[6]- Atualizar estoque\n[7]- Sair\n")
    opcao = input()

    if opcao == '1':
      loja.listar_produtos()
        
    elif opcao == '2':
      while True:
        try:
          nome = input("Digite o nome do produto: ")
          preco = input("Informe o preço do produto: ")
          estoque = input("Informe o estoque do produto: ")
          loja.adicionar(nome, preco, estoque)
          break
        except ValueError as e:
          print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '3':
      while True:
        try:
          nome = input("Digite o nome do produto: ")
          loja.buscar(nome)
          break
        except ValueError as e:
          print("Erro: ", e, " Tente novamente.\n")

    elif opcao == '4':
      while True:
        try:
          nome = input("Informe o nome do produto: ")
          loja.excluir(nome)
          break
        except ValueError as e:
          print("Erro: ", e, " Tente novamente.\n")

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