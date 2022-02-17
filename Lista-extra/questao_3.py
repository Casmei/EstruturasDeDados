
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
    return None

  def ver_item_da_caixa(self):
    pass

  def verifica_se_tem_conteudo_na_caixa(self):
    pass

caixa = Box()


print(caixa)
caixa.adicionar_item_na_caixa("Televisão")
print(caixa)
caixa.adicionar_item_na_caixa("Televisão2")
print(caixa)
caixa.remover_item_da_caixa()
print(caixa)
caixa.adicionar_item_na_caixa("Televisão2")
print(caixa)