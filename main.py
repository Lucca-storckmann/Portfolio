comando_inicial = input("Digite algo aqui: ")

if comando_inicial.upper() == "ABOUT":
    print("Portfolio do Lucca")
elif comando_inicial.upper() == "QUIT":
    print("Saindo do programa")
else:
    print("Erro na aplicação")
print("Até logo")