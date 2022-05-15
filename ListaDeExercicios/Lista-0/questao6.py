#Questão 6

valor_hora = 35
horas_trabalhadas = int(input('Horas Trabalhadas: '))

def salario (horas):
  if horas < 10:
    valor_final = ( horas * valor_hora ) * 0.2 #Valor do abono salárial
  else:
    valor_final = horas * valor_hora
  return valor_final

print(salario(horas_trabalhadas ))  

