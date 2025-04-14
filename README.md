📚 Sistema de Biblioteca (Arquitetura MVC)

Este é um projeto simples em Python para gerenciar ações de uma biblioteca, estruturado usando o padrão **MVC (Model-View-Controller)**. A ideia central é mostrar como separar responsabilidades e manter um código limpo, modular e de fácil manutenção.

## ---------------------------------------------------------------------------------------------

🧠 Objetivo

Permitir que o usuário execute ações como:

- Pesquisar livro
- Adicionar livro
- Modificar livro
- Excluir livro
- Sair do sistema

O menu é **dinâmico**, ou seja: basta adicionar uma nova opção na lista, criar a função correspondente, e ela já funcionará automaticamente — sem alterar o controlador.

## ---------------------------------------------------------------------------------------------

📁 Estrutura do Projeto
.
├── main.py          # Ponto de entrada da aplicação
├── model.py         # Dados e regras de negócio
├── view.py          # Interface com o usuário (entrada/saída)
├── controller.py    # Lógica de controle e fluxo do sistema
└── actions.py       # Funções principais (ações do menu)

## ---------------------------------------------------------------------------------------------

🧩 Lógica da Arquitetura

`main.py`
Arquivo principal, responsável apenas por iniciar o sistema.

## ---------------------------------------------------------------------------------------------

`model.py`
Contém os dados da aplicação. Neste caso, é uma lista de livros:

## ---------------------------------------------------------------------------------------------

`view.py`
Responsável por **exibir o menu** e **mostrar mensagens** ao usuário. Mantém toda a interação visual centralizada.

## ---------------------------------------------------------------------------------------------

`actions.py`
Contém as **ações que o usuário pode executar** (funções como `pesquisar_livro`, `adicionar_livro`, etc).  
Essas funções são chamadas de forma dinâmica, de acordo com a escolha do usuário.

## ---------------------------------------------------------------------------------------------

`controller.py`
Responsável por:

- Exibir o menu
- Obter a escolha do usuário
- Direcionar a ação correta

O truque aqui é o uso do `globals()` para **chamar dinamicamente funções** com base na escolha do usuário:

Esse formato permite que você apenas:

1. Adicione uma nova string no menu (`"Recomendar livro"`)
2. Crie a função `def recomendar_livro():` no `actions.py`

E pronto! A nova funcionalidade já estará funcionando ✨

## ---------------------------------------------------------------------------------------------

🔧 Como adicionar uma nova ação?

1. No `iniciar_sistema()` (em `controller.py`), adicione a nova opção:

```python
opcoes = [
    "Pesquisar livro",
    "Adicionar livro",
    "Recomendar livro",  # 👈 nova opção
    "Sair do sistema"
]
```

2. No `actions.py`, crie a função com o nome formatado:

```python
def recomendar_livro():
    mostrar_mensagem("Função de recomendar livro executada.")
```

Feito! Agora o menu já reconhece e executa essa nova ação automaticamente 🧩

## ---------------------------------------------------------------------------------------------

🛠 Requisitos

- Python 3.7+
- Terminal ou IDE com suporte a entrada de dados

## ---------------------------------------------------------------------------------------------

✍️ Autor

Desenvolvido por Leonardo Hoffmann Dias.
