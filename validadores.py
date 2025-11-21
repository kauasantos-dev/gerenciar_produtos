class ValidarProduto:
    @staticmethod
    def validar_nome(nome):
        if not nome.replace(" ", "").isalnum():
            raise ValueError("O nome do produto não deve conter caracteres especiais.")
        return nome.strip()
    
    @staticmethod
    def validar_preco(preco):
        try:
            preco = float(preco)
        except ValueError:
            raise ValueError("O preço do produto deve conter apenas números.")
        if preco <= 0:
            raise ValueError("O preço do produto não pode ser menor ou igual a 0 (zero).")
        return preco
    
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
        for produto in lista_produtos:
            if produto['Nome'].lower() == nome_produto.lower():
                return produto
        return False