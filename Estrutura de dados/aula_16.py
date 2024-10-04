# Dicionario
  # Utiliza index no formato e Keys e Values
  # Aceita string, integer, float, boolean...

aluno = {
  'nome': 'Ana',
  'idade': 16,
  'nota_final': 'A',
  'aprovação': True,
  'materias': ['Fisica', 'Matematica', 'Ingles']
}

print(aluno)

print(aluno.get('materias'))

print(len(aluno))

print(aluno.keys())
print(aluno.items())
print(aluno.values())