# Gerenciador de Tarefas Pessoais
# Sistema simples para organizar suas tarefas do dia a dia

# A lista é criada ANTES do loop para que os dados persistam entre os comandos.
# Se criássemos dentro do while, ela seria resetada a cada iteração — perdendo tudo!
tarefas = []

print("=== Gerenciador de Tarefas do Lucca ===")
print("Comandos disponíveis: ADD, LIST, QUIT")

while True:
    entrada = input("\nDigite um comando: ").strip()
    comando = entrada.upper()

    if comando == "QUIT":
        print("Encerrando o gerenciador. Até logo!")
        break

    elif comando.startswith("ADD"):
        partes = entrada.split(" ", 1)

        if len(partes) < 2 or partes[1].strip() == "":
            print("Erro: informe o nome da tarefa. Exemplo: ADD Estudar Python")
        else:
            nome_tarefa = partes[1].strip()
            tarefas.append(nome_tarefa)
            print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")

    elif comando == "LIST":
        if len(tarefas) == 0:
            print("Nenhuma tarefa cadastrada no momento.")
        else:
            print("\nSuas tarefas:")
            contador = 1
            for tarefa in tarefas:
                print(f"{contador}. {tarefa}")
                contador += 1

    else:
        print(f"Comando '{entrada}' não reconhecido. Tente ADD, LIST ou QUIT.")