from leitor_funcionarios import LeitorArquivoDeEmpregados
from funcionario import Funcionario


arquivo = './funcionarios.txt'

leitor = LeitorArquivoDeEmpregados(arquivo)
sacola_funcionarios = leitor.buscar_todos_funcionarios_em_uma_sacola()
leitor.fechar()

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


def cadastrar_funcionario(nome, cpf, cargo, salario):
    funcionario = Funcionario(nome, cpf, cargo, salario)
    sacola_funcionarios.adicionar_item(funcionario)
    return print(f"{funcionario.nome} Foi adicionado(a) com sucesso!")


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
        cadastrar_funcionario(nome, cpf, cargo, salario)

    if res == 2:
        print('--------------- LISTAGEM --------------- ')
        for i in sacola_funcionarios:
            print(i)
