class Box():

  def __init__(self):
      self.item = None

  def __str__(self) -> str:
    if self.item != False:
      return f"{self.item}"
    else:
      return "False"
    
  def adicionar_item_na_caixa(self, item):
    if self.item == None:
      self.item = item
      return self.item
    else:
      self.item = False
      return self.item

  def remover_item_da_caixa(self) -> None:
    self.item = None
    return self.item

  def ver_item_da_caixa(self):
    if self.item != None:
      return print(self.item)
    else:
      return False

  def verifica_se_tem_conteudo_na_caixa(self, item):
    return print(item == self.item)

caixa = Box()