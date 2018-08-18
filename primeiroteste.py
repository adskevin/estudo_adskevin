contador = int(0)
valor = 0
sair = True
while sair:
    valor = int(input())
    if valor>60:
        sair = False
    contador += 1
    print(contador)
print("Saiu.")
