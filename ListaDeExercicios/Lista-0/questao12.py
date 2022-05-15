def soma_matriz(vetor):
  resultados = []
  for i in range(0, 4):
    soma_linha = 0
    for j in range(0, 4):
      soma_linha = soma_linha + vetor[i][j]
    resultados.append(soma_linha)
  
  return resultados


matriz = [
  [1] * 4,
  [2] * 4,
  [3] * 4,
  [4] * 4,
]

print(soma_matriz(matriz))