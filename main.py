import sys

from auxiliares import uteis
from auxiliares import validadores
from configloja import gerenciar_loja

if __name__ == '__main__':

  loja = gerenciar_loja.Loja()
  print("===== GERENCIAMENTO DE PRODUTOS =====\n")
  while True:
    uteis.menu_opcoes()
    opcao = input()

    if opcao == '1':
      if not loja.listar_produtos():
        print("NÃO HÁ PRODUTOS CADASTRADOS.\n")
        
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

    elif opcao == '5' or opcao == '6':
      nome = input("Informe o nome do produto: ")

      if opcao == '5':
        preco = input("Informe o novo preço do produto: ")
        verificar_atualizacao = loja.atualizar_preco_estoque(nome, preco, '5', validadores.ValidarProduto.validar_preco)
        if verificar_atualizacao:
          print("PREÇO ATUALIZADO COM SUCESSO!\n")
        elif verificar_atualizacao is False:
          print("PRODUTO NÃO ENCONTRADO.\n")

      elif opcao == '6':
        estoque = input("Informe o novo estoque do produto: ")
        verificar_atualizacao = loja.atualizar_preco_estoque(nome, estoque, '6', validadores.ValidarProduto.validar_estoque)
        if verificar_atualizacao:
          print("ESTOQUE ATUALIZADO COM SUCESSO!\n")
        elif verificar_atualizacao is False:
          print("PRODUTO NÃO ENCONTRADO.\n")

    elif opcao == '7':
      print("\nEncerrando programa...")
      print("PROGRAMA ENCERRADO.")
      sys.exit(0)

    else:
      print("OPÇÃO INVÁLIDA. POR FAVOR, DIGITE UMA OPÇÃO DISPONÍVEL.\n")