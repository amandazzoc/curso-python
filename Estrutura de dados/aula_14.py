# Dicionario
  # Utiliza index no formato e Keys e Values
  # Aceita string, integer, float, boolean...

aluno = {
  'nome': 'Ana',
  'idade': 16,
  'nota_final': 'A',
  'aprovação': True
}

aluno.update(
  {
  'nome': 'Jose',
  'nota_final': 'B',
  }
)

print(aluno)
print(aluno.get('endereco')) # Não gera erro do que na forma tradicional, apenas retorna que é none
print(aluno.get('endereco', 'Não existe')) # Retorna o erro especificado

del aluno['idade'] # Remove o aluno 
print(aluno)