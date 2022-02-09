class Funcionario:
  def __init__(self, nome, cpf, cargo, salario):
    self.nome = nome
    self.cpf = cpf
    self.cargo = cargo
    self.salario = salario

  def __str__(self):
    espaço_nome = ((len(self.nome) - 30) * -1 ) * '-'
    espaço_cpf = ((len(self.cpf) - 15) * -1 ) * '-'
    espaço_cargo = ((len(self.cargo) - 20) * -1 ) * '-'
    return f'{self.nome} {espaço_nome}---- {self.cpf} {espaço_cpf}---- {self.cargo} {espaço_cargo}---- {self.salario}'
