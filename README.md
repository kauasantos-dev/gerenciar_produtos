# Sistema de Gerenciamento de Produtos  
![Python](https://img.shields.io/badge/Python-3.x-blue.svg) 
![Status](https://img.shields.io/badge/Status-Ativo-success)

Um projeto simples em **Python** que implementa um CRUD (Create, Read, Update, Delete) para gerenciamento de produtos, utilizando **POO** e persistência em **JSON**.  
O sistema é totalmente interativo pelo terminal.

---

## Pré-requisitos

Antes de executar, certifique-se de ter instalado:

- Python 3.x

- Git (para clonar o repositório)

---

## Funcionalidades

- **Listar produtos cadastrados**
- **Adicionar novo produto** (com validação de nome, preço e estoque)
- **Buscar produto por nome**
- **Excluir produto**
- **Atualizar preço de um produto**
- **Atualizar estoque de um produto**
- **Persistência dos dados em arquivo `.json`**
- **Tratamento de erros e validações**

---

## Tecnologias Utilizadas

- **Python 3**
- **JSON** para armazenamento
- **POO (Programação Orientada a Objetos)**
- **Bibliotecas nativas do Python:**
  - `os`
  - `sys`
  - `json`

---

## Estrutura do Projeto

```bash
gerenciar_produtos/
├── produtos.py              # Código principal
├── lista_produtos.json      # Arquivo de dados (gerado automaticamente)
└── README.md                # Documentação do projeto
```

---

## Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/kauasantos-dev/gerenciar_produtos.git
cd gerenciar_produtos
```

**2. Execute o programa**

```bash
python produtos.py
```

**3. Use o menu interativo**

```bash
===== GERENCIAMENTO DE PRODUTOS =====

Selecione uma opção abaixo (digite o número da opção):

[1]- Ver produtos cadastrados
[2]- Adicionar novo produto
[3]- Buscar produto
[4]- Excluir produto
[5]- Atualizar preço
[6]- Atualizar estoque
[7]- Sair
```

---

## Exemplo de uso

**1. Adicionando um produto:**

```bash
Digite o nome do produto: Arroz
Informe o preço do produto: 19.90
Informe o estoque do produto: 30

Produto adicionado com sucesso!
```

**2. Listando produtos:**

```bash
Produtos cadastrados:

Produto: Arroz | Preço: R$19.90 | Estoque: 30
```

**3. Atualizando preço:**

```bash
Informe o nome do produto: Arroz
Informe o novo preço do produto: 21.50

Preço atualizado com sucesso!
```

---

## Validações Implementadas

- Nome não pode conter caracteres especiais.

- Preço deve ser numérico e maior que zero.

- Estoque deve ser um número inteiro ≥ 0.

- Mensagens de erro amigáveis para o usuário.

---

## Aprendizados

Este projeto foi desenvolvido para praticar:

- Encapsulamento e métodos em POO.

- Persistência de dados com JSON.

- Criação de menus interativos no terminal.

- Validação e tratamento de erros em Python.

---

## Contribuição

Contribuições são bem-vindas! 
Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar o projeto.

---

## Licença

Este programa está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Autor

**Kavilly Kauã**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS) - IFRN**

**🌐 Contato:**

📧 [kavillykaua@gmail.com](mailto:kavillykaua@gmail.com)  
🌐 [GitHub | kauasantos-dev](https://github.com/kauasantos-dev)  