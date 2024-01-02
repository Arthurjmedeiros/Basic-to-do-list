# Defina uma lista vazia para armazenar as tarefas
lista_de_tarefas = []

# Função para adicionar uma nova tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a nova tarefa: ")
    lista_de_tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# Função para remover uma tarefa da lista
def remover_tarefa():
    if not lista_de_tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        print(f"{i}. {tarefa}")

    numero_tarefa = int(input("Digite o número da tarefa a ser removida: "))
    if 1 <= numero_tarefa <= len(lista_de_tarefas):
        tarefa_removida = lista_de_tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
    else:
        print("Número de tarefa inválido.")

# Função para exibir a lista de tarefas
def exibir_tarefas():
    if not lista_de_tarefas:
        print("A lista de tarefas está vazia.")
        return

    print("Lista de Tarefas:")
    for i, tarefa in enumerate(lista_de_tarefas, 1):
        print(f"{i}. {tarefa}")

# Loop principal
while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar Tarefa")
    print("2. Remover Tarefa")
    print("3. Exibir Tarefas")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        exibir_tarefas()
    elif opcao == "4":
        print("Obrigado por usar a lista de tarefas. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")