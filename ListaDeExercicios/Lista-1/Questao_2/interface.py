from traceback import print_tb
from produto import Produto
from sacola import Sacola


sacola = Sacola()

produto1 = Produto(254, "Feijao", 25)
produto2 = Produto(356, "Arroz", 36)
produto3 = Produto(234, "Soja", 12)
produto4 = Produto(166, "Shamppo", 16)
produto5 = Produto(324, "Cerveja", 35)

#Adicionar Produto
sacola.adicionar_item(produto1)
sacola.adicionar_item(produto1)
sacola.adicionar_item(produto1)
sacola.adicionar_item(produto2)
sacola.adicionar_item(produto3)
sacola.adicionar_item(produto4)
sacola.adicionar_item(produto5)

#Contar quantidade
print(sacola.quantidade_item(produto1))

#Remover produto
sacola.remover_item(produto1)

#Buscar produto
print(sacola.buscar_item(produto5))

#Tamanho sacola
print(sacola.tamanho_sacola())

#Verificar se contém determinado item
print(sacola.contem(produto2))
sacola.remover_item(produto2)
print(sacola.contem(produto2))

for produto in sacola:
  print(produto)