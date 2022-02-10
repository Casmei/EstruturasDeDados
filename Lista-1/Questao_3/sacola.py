class Sacola():

  def __init__(self):
    self.itens = list()
    self.count = 0

  def adicionar_item(self, item):
    self.itens.append(item)

  def remover_item(self, item):
    id = self.itens.index(item)
    return self.itens.pop(id)

  def buscar_item(self, item):
    for i in self.itens:
      if i == item:
        return item

  def quantidade_item(self, item):
    return sum(1 for i in self.itens if i == item)

  def tamanho_sacola(self):
    return len(self.itens)

  def contem(self, item):
    return item in self.itens

  def __iter__(self):
    return iter(self.itens)
