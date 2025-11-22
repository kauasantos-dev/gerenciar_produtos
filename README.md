# 🛒 Gerenciamento de Produtos (CLI)

Sistema simples de gerenciamento de produtos desenvolvido em Python, utilizando manipulação de arquivos JSON para salvar e carregar dados.
O projeto funciona totalmente pelo terminal e segue uma estrutura modular e organizada.

---

## 📌 Funcionalidades

- 📄 Listar produtos cadastrados

- ➕ Adicionar novos produtos

- 🔍 Buscar produto pelo nome

- ❌ Excluir produto

- 💲 Atualizar preço

- 📦 Atualizar estoque

- 💾 Salvamento automático em arquivo `.json`

---

## 📁 Estrutura do Projeto

```bash
gerenciar_produtos/
│
├── auxiliares/
│   ├── uteis.py
│   ├── validadores.py
│   └── __init__.py
│
├── configloja/
│   ├── caminho_arquivos.py
│   ├── gerenciar_arquivos.py
│   ├── gerenciar_loja.py
│   └── __init__.py
│
├── produtos/
│   └── lista_produtos.json
│
├── main.py
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🚀 Como Executar

**1. Clone o repositório:**

```bash
git clone https://github.com/kauasantos-dev/gerenciar_produtos.git
```

**2. Acesse a pasta do projeto:**

```bash
cd gerenciar_produtos
```

**3. Execute o programa:**

```bash
python main.py
```

---

## 🧠 Como o Sistema Funciona

- Todos os produtos são armazenados no arquivo:

```bash
produtos/lista_produtos.json
```

- O caminho do arquivo é gerado automaticamente usando os.path.abspath, garantindo compatibilidade entre computadores.

- Todas as regras de validação (nome, preço e estoque) ficam no módulo
auxiliares/validadores.py.

- Toda a lógica da loja (adicionar, excluir, buscar) está em
configloja/gerenciar_loja.py.

- A leitura e escrita do JSON é tratada em
configloja/gerenciar_arquivos.py.

---

## 📚 Tecnologias Utilizadas

- Python 3

- Manipulação de arquivos JSON

- Programação modular

- Validações usando classes utilitárias

---

## 🎓 Aprendizados

Durante o desenvolvimento deste projeto, pude aprender e praticar diversos conceitos importantes:

### ✔️ Organização de Projetos em Python

- Aprendi a estruturar um projeto real usando pastas, pacotes e módulos.

- Entendi a importância de separar responsabilidades (arquivos para validação, leitura de arquivos, lógica principal etc.).

### ✔️ Boas Práticas de Programação

- Apliquei funções com responsabilidade única.

- Evitei repetição de código usando utilitários e validadores.

- Estruturei o código para ser mais legível e de fácil manutenção.

### ✔️ Manipulação de Arquivos

- Aprendi a usar json.load() e json.dump() para persistir dados.

- Usei caminhos dinâmicos com os.path.abspath para garantir portabilidade.

### ✔️ Tratamento de Erros

- Melhorei meu entendimento sobre exceções, usando try/except para:

- validar entradas do usuário

- capturar erros de leitura de arquivo

- impedir valores inválidos no sistema

### ✔️ Pensamento Modular

- Compreendi como dividir um projeto em partes menores.

- Aprendi a importar corretamente módulos de pastas internas.

- Vi na prática como isso deixa o sistema mais organizado e escalável.

### ✔️ Lógica de Programação aplicada a um projeto real

- Trabalhei com listas, dicionários, loops e funções para manipular dados.

- Pratiquei fluxo de decisão em um menu interativo no terminal.

---

## 🔧 Melhorias Futuras

- Implementar interface gráfica (Tkinter / PyQt)

- Exportar produtos para CSV

- Criar testes automatizados

- Sistema de categorias para produtos

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request para melhorar o projeto.

---

## ⚖️ Licença

Este programa está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👤 Autor

**Kavilly Kauã | Estudante de Análise e Desenvolvimento de Sistemas (ADS) - IFRN**  

🌐 Contato:  

📧 **E-mail:** [kavillykaua@gmail.com](mailto:kavillykaua@gmail.com)  
💻 **GitHub:** [kauasantos-dev](https://github.com/kauasantos-dev)