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
├── .dockerignore
├── .gitignore
├── Dockerfile
├── LICENSE
├── main.py
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

## 🐳 Executando com Docker: 

Este projeto está **containerizado com Docker** e possui uma **imagem publicada no Docker Hub**, facilitando a execução sem necessidade de configurar o ambiente Python localmente.

### 📦 Imagem disponível no Docker Hub:
```bash
kauasantoss/gerenciar-produtos:latest
```

### ▶️ Executar a imagem

**⚠️ ATENÇÃO:** para que a **lista de produtos** fique salva em seu **host** (seu computador), é necessário **criar um volume Docker no momento da execução do container**.
A aplicação é executada dentro da pasta `/app` no container e o arquivo de produtos fica em:

```bash
/app/produtos/lista_produtos.json
```

### ▶️ Executar com volume (recomendado)

```bash
docker run -it -v ./produtos:/app/produtos kauasantoss/gerenciar-produtos:latest
```

**📌 Dessa forma:**

- Os dados ficam salvos na pasta `produtos/` do seu computador

- Ao parar ou remover o container, os produtos **não são perdidos**

- O container continua rodando normalmente em modo interativo

### ▶️ Executar sem volume (não recomendado)

```bash
docker run -it kauasantoss/gerenciar-produtos:latest
```

**⚠️ Nesse caso, os dados serão perdidos ao remover o container.**

📌 A aplicação será executada diretamente no terminal, exibindo o menu interativo do sistema de gerenciamento de produtos.

**⬇️ Informações adicionais:**

1. Para parar a execução, pressione `Ctrl + C` ou selecione a opção `7` do menu da aplicação.

2. Caso queira rodar a aplicação novamente após a primeira execução, digite o comando abaixo:

```bash
docker start -i ID_CONTAINER OU NOME DO CONTAINER
```

**⚠️ IMPORTANTE:**

Se o comando `docker run` for utilizado novamente para rodar o sistema, **outro container será criado**, o que **não é necessário**.

O `docker start` serve para executar o mesmo container criado inicialmente usando `docker run`. Isso evita que o usuário tenha que criar novos containers toda vez que quiser rodar o programa.

**❗OBSERVAÇÂO:** Para ver o ID e o nome do container, digite `docker ps -a`

---

## 🔧 Build local da imagem (opcional)

**⬇️ Caso queira construir a imagem localmente:**

```bash
docker build -t gerenciar-produtos .
docker run -it -v ./produtos:/app/produtos gerenciar-produtos:latest
```

---

## 📄 Sobre os arquivos Docker:

**Dockerfile:** define o ambiente da aplicação, incluindo a versão do Python e o comando de execução do sistema.

**.dockerignore**: evita que arquivos desnecessários (como .git, caches e ambientes locais) sejam incluídos na imagem, tornando o build mais leve e eficiente.

---

## 🧠 Como o Sistema Funciona

- Todos os produtos são armazenados no arquivo:

```bash
produtos/lista_produtos.json
```

- O caminho do arquivo é gerado automaticamente durante a execução da aplicação.

- Todas as regras de validação (nome, preço e estoque) ficam no módulo
auxiliares/validadores.py.

- Toda a lógica da loja (adicionar, excluir, buscar) está em
configloja/gerenciar_loja.py.

- A leitura e escrita do JSON é tratada em
configloja/gerenciar_arquivos.py.

---

## 📚 Tecnologias Utilizadas

- Python 3

- Docker

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

### ✔️ Containerização com Docker

Aprendizado sobre empacotamento da aplicação, criação de imagens e execução em ambientes isolados.

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

Este programa está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👤 Autor

**Kauã Santos | Estudante de Análise e Desenvolvimento de Sistemas (ADS) - IFRN**  

**📞 Contato:**  

📧 **E-mail:** [kavillykaua@gmail.com](mailto:kavillykaua@gmail.com)  
💻 **GitHub:** [github.com/kauasantos-dev](https://github.com/kauasantos-dev)  
🌐 **LinkedIn:** [www.linkedin.com/in/kauasantos1](https://www.linkedin.com/in/kauasantos1)