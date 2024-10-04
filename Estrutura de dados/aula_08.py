# Tuples
  # Armazenar mais de uma infromação em variáveis
  # Manter a sequencia dos dados em uma variável
  # Não podem ser alteradas (Immutable)

cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

print(cores_list)
print(cores_tuple)

print(type(cores_list))
print(type(cores_tuple))

duas_listas = cores_list * 2
duas_tuples = cores_tuple * 2
print(duas_listas)
print(duas_tuples)

cores_list.append('Roxo') # permitido
cores_tuple.append('Roxo') # erro

# Quando a lista não deve ser alterada, recomedado usar tuple
# Listas gastam um espaço maior de memória do que as tuple
# As tuples são mais rápidas
