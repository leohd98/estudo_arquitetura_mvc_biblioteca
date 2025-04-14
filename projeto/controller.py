from model import *
from view import *
from actions import *



def obter_escolha_usuario(opcoes):
    while True:
        try:
            escolha = int(input('Escolha uma opção: '))
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                mostrar_mensagem(f"\033[91mOpção inválida! Digite um número entre 1 e {len(opcoes)}.\033[0m")
        except ValueError:
            mostrar_mensagem("\033[91mEntrada inválida! Por favor, digite apenas números.\033[0m")



def direcionador(escolha, opcoes):
    valor_escolhido = opcoes[escolha - 1]
    valor_formatado = valor_escolhido.lower().replace(" ", "_")

    if valor_formatado in globals():
        globals()[valor_formatado]()  # Chama a função dinamicamente
    else:
        mostrar_mensagem(f"Função '{valor_formatado}()' ainda não foi implementada.")



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