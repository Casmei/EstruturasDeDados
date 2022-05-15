#Questão 11

def media(lista):
  return sum(lista) / len(lista)

def soma_matriz(vetor):
  resultados = []
  for i in range(0, 4):
    for j in range(0, 4):
      resultados.append(vetor[i][j])
  print(resultados)
  return media(resultados)

matriz = [
[1] * 4,
[2] * 4,
[3] * 4,
[4] * 4,
]

print(soma_matriz(matriz))