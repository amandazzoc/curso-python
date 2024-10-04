# Dicionario
  # Utiliza index no formato e Keys e Values
  # Aceita string, integer, float, boolean...

aluno = {
  'nome': 'Ana',
  'idade': 16,
  'nota_final': 'A',
  'aprovação': True
}

for x in aluno: # Apenas as chaves
  print(x)

print()

for x in aluno.keys(): # Apenas as chaves
  print(x)

print()

for x in aluno.values(): # Apenas os valores
  print(x)

print()

for x in aluno.items(): # Chaves e valores
  print(x)

print()

for keys, values in aluno.items():
  print(keys, values)