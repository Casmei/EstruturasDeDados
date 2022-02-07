from contador import Contador
click = Contador()
print(click)

click.incrementar()
print(click)

click.incrementar()
click.incrementar()
click.incrementar()
click.incrementar()
print(click)

click.zerar_contador()
print(click)

click.set_valor(10000)
print(click)

click.zerar_contador()
print(click)

for i in range(0, 100001):
  click.incrementar()
print(click)