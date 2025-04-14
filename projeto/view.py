def mostrar_menu(opcoes):
    print("\n" * 3)
    print("\033[92mSISTEMA BIBLIOTECA")
    print("--------------------------------------------------")
    print("Escolha o que deseja fazer:\n")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}) {opcao}")
    print("\033[0m")

def mostrar_mensagem(mensagem):
    print(mensagem)