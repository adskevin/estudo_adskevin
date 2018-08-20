contador = int(0)
valor = 0
sair = True
nome = ""
nomes = []

def leNome (str):
    nomes [contador] = input(str)
    return nome;

while sair:
    nome = leNome("Digite um nome: ")
    if nome == "sair":
        sair = False
    else:
        print("Digite sair para sair: ")
    contador += 1
    print(contador)
print("Saiu.")
