#Questão 11

def soma_matriz(vetor):
  resultados = 0
  for i in range(0, 4):
    soma_linha = 0
    for j in range(0, 4):
      soma_linha = soma_linha + vetor[i][j]
    resultados += soma_linha
  
  return resultados

matriz = [
[1] * 4,
[1] * 4,
[1] * 4,
[1] * 4,
]

print(soma_matriz(matriz))