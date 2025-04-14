## Sistema de Biblioteca Usando Arquitetura MVC
Este é um sistema de gerenciamento de livros em uma biblioteca usando a arquitetura MVC, desenvolvido em Python. O sistema permite ao usuário realizar diversas operações, como pesquisar, adicionar, modificar, excluir livros ou sair do sistema.

## Funcionalidades
Pesquisar livro: Permite ao usuário buscar por um livro.

Adicionar livro: Permite adicionar um novo livro à lista da biblioteca.

Modificar livro: Permite modificar o título de um livro existente.

Excluir livro: Permite excluir um livro da biblioteca.

Sair do sistema: Encerra o programa.

## Estrutura do Projeto
O projeto é dividido em cinco arquivos principais:

### actions.py
Contém as funções que executam as ações específicas do sistema. Cada função exibe uma mensagem indicando a execução da ação correspondente.

Funções:

pesquisar_livro(): Simula a pesquisa de um livro.

adicionar_livro(): Simula a adição de um livro.

modificar_livro(): Simula a modificação de um livro.

excluir_livro(): Simula a exclusão de um livro.

sair_do_sistema(): Exibe a mensagem de saída e encerra o programa.

### controller.py
É responsável por gerenciar a interação do usuário com as opções do sistema. Ele captura a escolha do usuário, valida a entrada e direciona para a função correspondente no arquivo actions.py. Além disso, possui a lógica para controlar o fluxo do programa.

Funções:

obter_escolha_usuario(): Recebe a escolha do usuário e valida a entrada.

direcionador(): Direciona a execução para a função correspondente com base na escolha do usuário.

pesquisar_livro_controller(): Chama a função de pesquisa de livro.

adicionar_livro_controller(): Chama a função de adicionar livro.

modificar_livro_controller(): Chama a função de modificar livro.

excluir_livro_controller(): Chama a função de excluir livro.

sair_do_sistema_controller(): Chama a função de sair do sistema.

iniciar_sistema(): Exibe o menu inicial e aguarda a interação do usuário.

### main.py
É o ponto de entrada do programa. Ele importa e chama a função iniciar_sistema() do arquivo controller.py para iniciar o sistema.

### model.py
Contém os dados (livros) que o sistema manipula. A lista de livros é convertida para maiúsculas para garantir a consistência na manipulação dos dados.

### view.py
Responsável pela interação com o usuário através da interface de linha de comando. Ele exibe o menu de opções e as mensagens do sistema.

Funções:

mostrar_menu(): Exibe o menu com as opções disponíveis.

mostrar_mensagem(): Exibe uma mensagem personalizada no console.

obter_dado_int(): Recebe uma entrada do usuário e a converte para um número inteiro.

## Estrutura de Arquivos

├── actions.py         # Contém as funções de ações do sistema

├── controller.py      # Controlador do fluxo de interações

├── main.py            # Ponto de entrada para o sistema

├── model.py           # Contém os dados (livros)

└── view.py            # Exibe o menu e interage com o usuário

Contribuições
Sinta-se à vontade para fazer melhorias no projeto, sugerir novas funcionalidades ou corrigir eventuais bugs.

Desenvolvido por Leonardo Hoffmann Dias
