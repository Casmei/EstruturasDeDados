#Questão 3

def verifica_sinal(numero):
  if numero > 0:
    return True
  elif numero < 0:
    return False
  else:
    return None

print(verifica_sinal(0))