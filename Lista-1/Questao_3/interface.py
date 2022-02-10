from leitor_funcionarios import LeitorArquivoDeEmpregados
from funcionario import Funcionario


arquivo = './funcionarios.txt'

leitor = LeitorArquivoDeEmpregados(arquivo)
sacola_funcionarios = leitor.buscar_todos_funcionarios_em_uma_sacola()
leitor.fechar()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def cadastrar_funcionario(nome, cpf, salario, cargo):
    funcionario = Funcionario(nome, cpf, salario, cargo)
    sacola_funcionarios.adicionar_item(funcionario)
    with open(arquivo, 'a') as f:
      f.write(str(funcionario))


flag = True
while flag:
    print(" --------------- MENU --------------- ")
    print(" [1] - Cadastrar novo usuário ")
    print(" [2] - Listar funcionários ")
    print(" [3] - Buscar funcionário pelo CPF ")
    print(" [4] - Fechar programa ")

    res = int(input(" Digite o número da operação: "))

    if res == 1:
        nome = input(" Informe o nome completo do funcionário: ")
        cpf = input(" Informe o cpf do funcionário: ")
        cargo = input(" Informe o cargo do funcionário: ")
        salario = float(input(" Informe o salario do funcionário: "))
        cadastrar_funcionario(nome, cpf, salario, cargo)

    if res == 2:
        print('--------------- LISTAGEM --------------- ')

        for i in sacola_funcionarios:
          espaço_nome = ((len(i.nome) - 30) * -1 ) * '-'
          espaço_cpf = ((len(i.cpf) - 15) * -1 ) * '-'
          espaço_salario = ((len(i.salario) - 20) * -1 ) * '-'

          print(f'{i.nome} {espaço_nome}---- {i.cpf} {espaço_cpf}---- {i.salario} {espaço_salario}---- {i.cargo}')

    print('\n\n')