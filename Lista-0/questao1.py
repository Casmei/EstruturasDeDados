#Questão 1

def imc(altura, peso):
  res = peso / (altura * altura)
  return res

print(imc(1.75, 60))