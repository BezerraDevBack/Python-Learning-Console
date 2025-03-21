# Função para exibir o menu principal
def exibir_menu_principal():
    print("\n=== Menu Principal ===")
    print("1. Aprender")
    print("2. Fazer um Quiz")
    print("3. Sair")


# Função para exibir o menu de aprendizado
def exibir_menu_aprender():
    print("\n=== Modo Aprender ===")
    print("1. Como exibir mensagens na tela? (print())")
    print("2. Como receber dados do usuário? (input())")
    print("3. Voltar ao Menu Principal")


# Função que gerencia o modo de aprendizado
def aprender():
    while True:
        exibir_menu_aprender()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            ensinar_print()
        elif escolha == '2':
            ensinar_input()
        elif escolha == '3':
            break  # Volta para o menu principal
        else:
            print("Opção inválida. Tente novamente.")


# Função que ensina o comando print()
def ensinar_print():
    print("\n--- Como exibir mensagens na tela? ---")
    print("O comando 'print()' é usado para exibir mensagens no console.")
    print("Exemplo de uso: print('Olá, Mundo!')")
    print("Saída esperada: Olá, Mundo!")
    if deseja_fazer_quiz():
        quiz_print()


# Função que ensina o comando input()
def ensinar_input():
    print("\n--- Como receber dados do usuário? ---")
    print("O comando 'input()' é usado para receber dados do usuário via console.")
    print("Exemplo de uso: nome = input('Qual é o seu nome? ')")
    print("Saída esperada: Qual é o seu nome? (usuário digita algo)")
    if deseja_fazer_quiz():
        quiz_input()


# Função que pergunta se o usuário quer fazer um quiz
def deseja_fazer_quiz():
    resposta = input("Deseja fazer um quiz sobre o tema? (S/N): ").upper()
    return resposta == 'S'


# Função que exibe o quiz sobre o comando print()
def quiz_print():
    print("\n--- Quiz sobre 'print()' ---")
    print("1. Qual comando é usado para exibir mensagens na tela?")
    print("a) input()")
    print("b) print()")
    print("c) display()")
    
    resposta = input("Resposta: ").lower()
    
    if resposta == 'b':
        print("Correto! Muito bem.")
    else:
        print("Errado. A resposta correta é: b) print().")


# Função que exibe o quiz sobre o comando input()
def quiz_input():
    print("\n--- Quiz sobre 'input()' ---")
    print("1. Qual comando é usado para receber dados do usuário?")
    print("a) input()")
    print("b) print()")
    print("c) read()")
    
    resposta = input("Resposta: ").lower()
    
    if resposta == 'a':
        print("Correto! Muito bem.")
    else:
        print("Errado. A resposta correta é: a) input().")


# Função que exibe o quiz geral sobre Python
def quiz_geral():
    print("\n--- Quiz Geral sobre Python ---")
    perguntas = [
        {
            "pergunta": "Quem criou a linguagem Python?",
            "opcoes": ["a) Guido van Rossum", "b) Dennis Ritchie", "c) James Gosling"],
            "resposta": "a"
        },
        {
            "pergunta": "Em que ano o Python foi lançado?",
            "opcoes": ["a) 1989", "b) 1991", "c) 1995"],
            "resposta": "b"
        },
        {
            "pergunta": "De onde vem o nome Python?",
            "opcoes": ["a) Uma cobra", "b) Uma série de TV", "c) Uma linguagem antiga"],
            "resposta": "b"
        }
    ]

    for questao in perguntas:
        print("\n" + questao["pergunta"])
        for opcao in questao["opcoes"]:
            print(opcao)
        
        resposta = input("Resposta: ").lower()
        
        if resposta == questao["resposta"]:
            print("Correto! Muito bem.")
        else:
            print(f"Errado. A resposta correta é: {questao['resposta']}.")


# Função principal que executa o programa
def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            aprender()  # Acessa o modo aprender
        elif opcao == '2':
            quiz_geral()  # Inicia o quiz geral sobre Python
        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break  # Sai do programa
        else:
            print("Opção inválida. Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    main()
