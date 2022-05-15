class Contador():

  def __init__(self):
    self.valor = 0

  def get_valor(self):
    return self.valor

  def set_valor(self, novo_valor):

    self.valor = novo_valor
    return self.valor

  def __str__(self):
    '''Funcao para retornar a quantidade de cliques.'''
    display = Contador.exibir_display(self)
    return display

  def incrementar(self):
    '''- Quando utilizada, a funcao sempre incrementara 1 ao parametro.'''
    self.valor += 1
    return self.valor

  def exibir_display(self):
    """Funcao que retorna o valor acompanhado de zeros a esquerda.
    - Tem como limite de incrementacoes o valor 9999"""
    if self.valor >= 10000:
      return f"9999"
    if self.valor < 10:
      return f"000{self.valor}"
    elif self.valor >= 10 and  self.valor < 100:
      return f"00{self.valor}"
    elif self.valor >= 100 and self.valor < 1000:
      return f"0{self.valor}"

    else:
      return f"{self.valor}"

  def zerar_contador(self):
    """Funcao para retornar ao valor inicial, zero."""
    self.valor = 0
