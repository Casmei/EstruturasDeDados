from funcionario import Funcionario
from sacola import Sacola


class LeitorArquivoDeEmpregados:

  def __init__(self, nome_arquivo):
    self.nome_arquivo = nome_arquivo
    self.arquivo = open(self.nome_arquivo, 'r', encoding='UTF-8')

  def fechar(self):
    self.arquivo.close()
    self.nome_arquivo = None

  def proximo_funcionario(self):
    self.arquivo
    nome = self.arquivo.readline().rstrip()

    if nome == "":
      return None

    cpf = self.arquivo.readline().rstrip()
    salario = self.arquivo.readline().rstrip()
    cargo = self.arquivo.readline().rstrip()

    return Funcionario(nome, cpf, cargo, salario)

  def buscar_todos_funcionarios_em_uma_sacola(self):
    sacola_funcionarios = Sacola()
    funcionario = self.proximo_funcionario()

    while funcionario != None:
      sacola_funcionarios.adicionar_item(funcionario)
      funcionario = self.proximo_funcionario()

    return sacola_funcionarios
