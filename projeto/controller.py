import sys
from model import *
from view import *
from actions import *



def obter_escolha_usuario(opcoes):
    while True:
        try:
            escolha = obter_dado_int('Escolha uma opção: ')
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                mostrar_mensagem(f"\033[91mOpção inválida! Digite um número entre 1 e {len(opcoes)}.\033[0m")
        except ValueError:
            mostrar_mensagem("\033[91mEntrada inválida! Por favor, digite apenas números.\033[0m")



def direcionador(escolha, opcoes):
    valor_escolhido = opcoes[escolha - 1]
    valor_formatado = valor_escolhido.lower().replace(" ", "_")
    controller_function_name = f"{valor_formatado}_controller"
    
    try:
        # Usando getattr() para buscar a função controladora dinamicamente
        controller_function = getattr(sys.modules[__name__], controller_function_name)
        controller_function()  # Chama a função do controlador
    except AttributeError:
        mostrar_mensagem(f"Controlador '{controller_function_name}()' não encontrado.")



def pesquisar_livro_controller():
    # Aqui você pode adicionar lógica extra, se necessário
    pesquisar_livro()  # Chama a função na camada de actions



def adicionar_livro_controller():
    # Lógica extra do controlador, se necessário
    adicionar_livro()  # Chama a função na camada de actions



def modificar_livro_controller():
    # Lógica extra do controlador, se necessário
    modificar_livro()  # Chama a função na camada de actions



def excluir_livro_controller():
    # Lógica extra do controlador, se necessário
    excluir_livro()  # Chama a função na camada de actions



def sair_do_sistema_controller():
    # Lógica extra do controlador, se necessário
    sair_do_sistema()  # Chama a função na camada de actions



def iniciar_sistema():
    opcoes = [
        "Pesquisar livro",
        "Adicionar livro",
        "Modificar livro",
        "Excluir livro",
        "Sair do sistema"
    ]
    while True:
        mostrar_menu(opcoes)
        escolha = obter_escolha_usuario(opcoes)
        direcionador(escolha, opcoes)
