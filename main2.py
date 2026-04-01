while True:
    comando_inicial = input("Digite algo aqui: ")

    if comando_inicial.upper() == "ABOUT":
        print("Portfolio do Lucca")
    elif comando_inicial.upper() == "ADD":
        num_projetos = int(input("Quantos projeto deseja cadastrar: "))
        if num_projetos <= 0:
             print("Erro")
        else:
            for projeto in range(num_projetos):
                nome_projeto = input("Qual o nome do projeto: ")
                print("Projeto cadastrado.")
    elif comando_inicial.upper() == "QUIT":
        print("Saindo do programa")
    break
else:
    print("Erro na aplicação")
    print("Até logo")