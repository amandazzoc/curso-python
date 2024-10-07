carrosEstoque = ['BMW X6', 'BMW i5', 'BMW i8']

carro = input('Insira o nome do carro que deseja comprar: ')

if carro in carrosEstoque:
  print('Carro em estoque')
else:
  print('Carro não está em estoque')
