import re

class ValidarProduto:
    @staticmethod
    def validar_nome(nome):
        if not nome.replace(" ", "").isalnum():
            raise ValueError("O nome do produto não deve conter caracteres especiais.")
        return nome.strip()
    
    @staticmethod
    def validar_preco(preco):
        estrutura_preco = r'^(?:R\$)?\s*([0-9]+)(\.[0-9]{3})*(\,[0-9]+)?$'
        if re.match(estrutura_preco, preco):
            return float(
                preco
                .replace(".", "")
                .replace(",", ".")
                .replace("R$", "")
                .replace(" ", "")
            )
        raise ValueError("Preço inválido. Por favor, informe um valor válido. (EX: R$20, R$ 20.00, 20...).\n")

    @staticmethod
    def validar_estoque(estoque):
        try:
            estoque = int(estoque)
        except ValueError:
            raise ValueError("O estoque deve conter apenas números.")
        if estoque < 0:
            raise ValueError("O estoque não pode ser menor que 0 (zero).")
        return estoque
    
    @staticmethod
    def verificar_existencia_produto(nome_produto, lista_produtos):
        if not lista_produtos:
            return False
        for produto in lista_produtos:
            if produto['Nome'].lower() == nome_produto.lower():
                return produto
        return False