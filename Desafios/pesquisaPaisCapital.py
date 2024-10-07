paisesCapital = {
  'Afeganistao':'Cabul',
  'África do Sul':'Pretória',
  'Canada':'Ottawa',
  'Chile':'Santigo',
  'Brasil':'Brasilia'
  }

pais = input('Escolha um país: ')

if pais in paisesCapital:
  print(f'A capital do {pais} é {paisesCapital[pais]}')
else:
  print('Desculpe, não temos informações sobre a capital desse país')