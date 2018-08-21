finaliza = True
limitePessoas = 2
aNome = []
aSalario = []
def testeMenu(arg):
        if arg == 0:
            print("Finalizar.")
            finalizaPrograma()
            global finaliza
            finaliza = False
        elif arg == 1:
            print("Cadastrar.")
            cadastra()
        elif arg == 2:
            print("Lista.")
            lista()
        elif arg == 3:
            print("Mostra salário de uma pessoa.")
        elif arg == 4:
            print("Mostra o nome das pessoas que ganham acima da média.")
        elif arg == 5:
            print("Aplique percentual de aumento a todos.")
        elif arg == 6:
            print("Aplique percentual de aumento somente para aqueles que ganham abaixo da média.")
        else: print("\nValor incorreto.")

def finalizaPrograma():
    print("Entrou finaliza")

def digitaSalario():
    print("Entrou digitaSalario")
    try:
        salario = float(input("\nDigite o salário deste funcionário: R$ "))
    except:
        print("Erro, rente novamente.")
        return digitaSalario
    return salario

def cadastra():
    global aNome
    global aSalario
    global limitePessoas
    if len(aNome) < limitePessoas:
        try:
            nome = str(input("\nDigite um nome: "))
        except:
            print("Erro, tente novamente.")
            return cadastra();
        aNome += [nome]
        aSalario += [digitaSalario()]

    else: print("Lista de pessoas cheia!")


def lista():
    global aNome
    print(aNome)
    global aSalario
    print(aSalario)

def escolhaMenu():
    try:
        valor = int(input("\nDigite: "))
    except:
        print("Erro.")
        return escolhaMenu();
    return valor;

while finaliza:
    menu = "\nMenu"
    menu += "\n-------------"
    menu += "\n0- Finaliza"
    menu += "\n1- Cadastra"
    menu += "\n2- Lista"
    menu += "\n3- Mostra salario de uma pessoa"
    menu += "\n4- Mostra o nome das pessoas que ganham acima da media"
    menu += "\n5- Aplique um percentual de aumento a todos"
    menu += "\n6- Aplique um percentual de aumento somente\npara aqueles que ganham abaixo da média"
    print(menu)
    testeMenu(escolhaMenu())
