def dobro(num):
  return num * 2

def quadrado(num):
  return dobro(num) ** 2

num = int(input('Digite um número: '))
print(f'O quadrado do dobro do número escolhido é: {quadrado(num)}')