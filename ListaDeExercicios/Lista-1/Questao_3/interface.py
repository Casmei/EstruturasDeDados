from leitor_funcionarios import LeitorArquivoDeEmpregados
from funcionario import Funcionario

arquivo = './funcionarios.txt'
  
def adicionar_funcionario_ao_arquivo(funcionario):
    with open(arquivo, 'a') as f:
        f.write(str(funcionario))

def mostrar_menu():
    print(" --------------- MENU --------------- ")
    print(" [1] - Cadastrar novo usuário ")
    print(" [2] - Listar funcionários ")
    print(" [3] - Buscar funcionário pelo CPF ")
    print(" [4] - Fechar programa ")
    
    return int(input(" Digite o número da operação: "))

def executa_opcao_do_menu(res, sacola_funcionarios):
  match res:
        case 1:
          cadastrar_novo_funcionarios(sacola_funcionarios)
          return True
          
        case 2:
          listar_todos_funcionarios(sacola_funcionarios)
          return True
          
        case 3:
          buscar_funcionario_por_cpf(sacola_funcionarios)
          return True
          
        case 4:
          exibir_mensagem_de_encerramento()
          return False
        
        case _:
          caso_opcao_inválida()
          return True

def caso_opcao_inválida():
    print('\nOpção inválida!')
    input("Digite qualquer tecla para tentar novamente...")

def exibir_mensagem_de_encerramento():
    print('\nPrograma Fechado!')

def buscar_funcionario_por_cpf(sacola_funcionarios):
    cpf_buscado = input(" Informe o cpf do funcionário: ")
    
    def busca_cpf(i):
      return i.cpf == cpf_buscado
    
    funcionario_encontrado = sacola_funcionarios.encontre(busca_cpf)
    
    if funcionario_encontrado:
      print(f"\n - Nome: {funcionario_encontrado.nome}")
      print(f" - Cargo: {funcionario_encontrado.cargo}")
      print(f" - Salario: {funcionario_encontrado.salario}")
    else:
      print('Nenhum funcionario foi encontrado')

def listar_todos_funcionarios(sacola_funcionarios):
    print('--------------- LISTAGEM --------------- ')
          
    for i in sacola_funcionarios:
      espaço_nome = ((len(i.nome) - 30) * -1 ) * ' '
      espaço_cpf = ((len(i.cpf) - 15) * -1 ) * ' '
      espaço_salario = ((len(str(i.salario)) - 20) * -1 ) * ' '

      print(f'{i.nome} {espaço_nome} | {i.cpf} {espaço_cpf} | {i.salario} {espaço_salario} | {i.cargo}')

def cadastrar_novo_funcionarios(sacola_funcionarios):
    nome = input(" Informe o nome completo do funcionário: ")
    cpf = input(" Informe o cpf do funcionário: ")
    cargo = input(" Informe o cargo do funcionário: ")
    salario = float(input(" Informe o salario do funcionário: "))
    
    funcionario = Funcionario(nome, cpf, salario, cargo)
    sacola_funcionarios.adicionar_item(funcionario)
    
    adicionar_funcionario_ao_arquivo(funcionario)
  
def ler_sacola_do_arquivo():
    leitor = LeitorArquivoDeEmpregados(arquivo)
    sacola_funcionarios = leitor.buscar_todos_funcionarios_em_uma_sacola()
    leitor.fechar()
    return sacola_funcionarios
      
def comeca_interface():
  sacola_funcionarios = ler_sacola_do_arquivo()
  
  flag = True
  while flag:
      res = mostrar_menu()
      flag = executa_opcao_do_menu(res, sacola_funcionarios)
      print('\n')
      
comeca_interface()