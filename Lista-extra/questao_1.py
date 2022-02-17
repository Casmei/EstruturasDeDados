
class Cube():
  def __init__(self, altura, largura):
      self.altura = altura
      self.largura = largura

  def get_altura(self):
    return self.altura

  def get_largura(self):
    return self.largura

  def set_altura(self,altura):
    self.altura = altura
    return self.altura

  def set_largura(self, largura):
    self.largura = largura
    return self.largura
    
  def obter_area_quadrado(self):
    area_quadrado = self.altura * self.largura
    return area_quadrado

  def __str__(self):
    return f"{self.altura}x{self.largura}"

quadrado = Cube(5, 5)
print(quadrado.obter_area_quadrado())

