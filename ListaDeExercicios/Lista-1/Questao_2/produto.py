class Produto:
  def __init__(self, id, nome, valor):
      self.id= id
      self.nome = nome
      self.valor = valor

  def __str__(self):
      return f"{self.id} {self.nome}\t{self.valor}"