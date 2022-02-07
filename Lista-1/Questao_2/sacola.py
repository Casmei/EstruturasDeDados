class Sacola():
  def __init__(self):
    self.itens = list()

  def adicionar_item(self, item):
    self.itens.append(item)

  def remover_item(self, item):
    id = self.itens.index(item)
    return self.itens.pop(id)

  def buscar_item(self, item):
    id = self.itens.index(item)
    return self.itens[id]

  def quantidade_item(self, item):
    quantidade = 0
    for i in self.itens:
      if item == i:
        quantidade += 1
    return f"Total de {item.nome}: {quantidade}qts"

  def tamanho_sacola(self):
    return len(self.itens)
  
  def contem(self, item):
    if item in self.itens:
      return f"{item.nome} esta na sacola!"
    else:
      return f"{item.nome} nao esta na sacola!"

  def __iter__(self):
    return Iterador(self.itens)

class Iterador:
  def __init__(self, lista):
      self.itens = lista
      self.atual = 0 

  def __next__(self):
    if self.atual < len(self.itens):
      item = self.itens[self.atual]
      self.atual += 1
      return item
    else:
      raise StopIteration