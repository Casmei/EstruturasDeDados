#Questão 9

lista = []
loop = int(input('Quantas vezes deseja que o laço se repita? '))
for i in range(1, loop + 1):
  valor = input(f"Digite o {i}º valor: ")
  lista.append(valor)
print("\n",lista)