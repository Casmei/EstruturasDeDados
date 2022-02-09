class Funcionario:
  def __init__(self, nome, cpf, salario, cargo):
      self.nome = nome
      self.cpf = cpf 
      self.cargo = cargo
      self.salario = salario

  def __str__(self):
    return f'{self.nome} ---- {self.cargo} ---- {self.cpf} ---- {self.salario}'
