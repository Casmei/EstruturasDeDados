from leitor_funcionarios import LeitorArquivo
from sacola import Sacola
from funcionario import Funcionario


arquivo = './dados.txt'
leitor = LeitorArquivo(arquivo)
sacola = Sacola()

leitor.abrir()
funcionarios = leitor.funcionarios_lista()

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def cadastrar_funcionario(nome, cpf, cargo, salario):
    funcionario = Funcionario(nome, cpf, cargo, salario)
    sacola.adicionar_item(funcionario)
    return print(f"{funcionario.nome} Foi adicionado(a) com sucesso!")




flag = True
print(sacola)
while flag:
    print(" --------------- MENU --------------- ")
    print(" [1] - Cadastrar novo usuário ")
    print(" [2] - Listar funcionários ")
    print(" [3] - Buscar funcionário pelo CPF ")
    print(" [4] - Fechar programa ")

    res = int(input(" Digite o número da operação: "))

    if res == 1:
        flag = False
        nome = input(" Informe o nome completo do funcionário: ")
        cpf = int(input(" Informe o cpf do funcionário: "))
        cargo = input(" Informe o cargo do funcionário: ")
        salario = float(input(" Informe o salario do funcionário: "))
        cadastrar_funcionario(nome, cpf, cargo, salario)

    if res == 2:
        print('--------------- LISTAGEM --------------- ')
        for i in sacola:
            print(i)
