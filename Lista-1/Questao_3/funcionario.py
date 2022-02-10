class Funcionario:
  def __init__(self, nome, cpf, salario, cargo):
    self.nome = nome
    self.cpf = cpf
    self.salario = salario
    self.cargo = cargo

  def __str__(self):
    return f'{self.nome}\n{self.cpf}\n{self.salario}\n{self.cargo}\n'