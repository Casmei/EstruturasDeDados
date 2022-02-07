#Questão 4

def verifica_divisibilidade(numero):
  if numero%2 == 0 and numero != 0:
    return True
  elif numero%2 != 0:
    return False
  elif numero == 0:
    return None

print(verifica_divisibilidade(10))