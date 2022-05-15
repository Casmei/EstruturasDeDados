#QUESTÃO 7


def soma(num1, num2):
  resultado = num1 + num2
  return resultado

def mult(num1, num2):
  resultado = num1 * num2
  return resultado

def div(num1, num2):
  if num1 or num2 == 0:
    return False
  else:
    resultado = num1 / num2
    return resultado

flag = True
while flag:
  print ('\n1 - Somar dois valores.')
  print ('2 - Multiplicar dois valores.')
  print ('3 - Dividir dois valores.')
  print ('4 - Sair do programa.')
  
  res = int(input( '\n* Selecione a opção desejada: ' ))

  if res == 1:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado = soma(num1, num2)
    print(f'\n- O resultado entre a soma de {num1} e {num2} é igual a {resultado}')
  elif res == 2:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    resultado = mult(num1, num2)
    print(f'\n- O resultado entre a multiplicação de {num1} e {num2} é igual a {resultado}')
  elif res == 3:
    num1 = int(input('\nDigite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if div(num1, num2):
      resultado = div(num1, num2)
      print(f'\n- O resultado entre a divisão de {num1} e {num2} é igual a {resultado}')
    else:
      print('Operação inválida!')
  elif res == 4:
    print('Obrigado, voltei sempre!')
    flag = False
  else:
    print('Valor inválido, digite novamente!')

