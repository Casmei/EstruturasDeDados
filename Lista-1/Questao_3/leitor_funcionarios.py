from funcionario import Funcionario
from sacola import Sacola
class LeitorArquivo:

  def __init__(self, nome_arquivo):
    self.nome_arquivo = nome_arquivo
    self.arquivo = None

  def abrir(self):
    self.arquivo = open(self.nome_arquivo, 'r', encoding='UTF-8')

  def fechar(self):
    self.arquivo.close()
    self.nome_arquivo = None

  def proximo(self):
    nome = self.arquivo.readline().rstrip()
    if nome == "":
      return None
    cpf = self.arquivo.readline().rstrip()
    salario = self.arquivo.readline().rstrip()
    cargo = self.arquivo.readline().rstrip()

    funcionario = Funcionario(nome, cpf, salario, cargo)
    Sacola().adicionar_item(funcionario)
    return funcionario

  def funcionarios_lista(self):
    sacola_funcionarios = Sacola()
    funcionario = self.proximo()
    while funcionario != None:
      sacola_funcionarios.adicionar_item(funcionario)
      funcionario = self.proximo()
    return sacola_funcionarios