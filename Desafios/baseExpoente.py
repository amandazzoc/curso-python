def potencia(base, expoente = 2):
  potencia = base ** expoente
  return potencia

base_usr = int(input('Digite a base: '))
expo_usr = input('Digite o expoente (default 2): ')

if expo_usr:
  print(f'O calculo entre a base {base_usr} e o expoente {expo_usr} é: {potencia(base_usr, int(expo_usr))}')
else:
  print(f'O calculo entre a base {base_usr} e o expoente 2 é: {potencia(base_usr)}')