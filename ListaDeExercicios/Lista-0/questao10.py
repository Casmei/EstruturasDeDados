#Questão 10

lista = []

def pares_lista(lista):
  par = []
  for i in lista:
    if i%2 == 0:
      par.append(i)
  return par
    

loop = int(input('Quantas vezes deseja que o laço se repita? '))
for i in range(1, loop + 1):
  valor = int(input(f"Digite o {i}º valor: "))
  lista.append(valor)
print(pares_lista(lista))