# Set (listas)
  # Similar a listas
  # Evita itens duplicados
  # Não utiliza index

list1 = set([1, 2, 3, 4, 5, 6]) # Transforma uma lista em set
s1 = {1, 2, 3, 4, 5, 6} # Faz um set direto

print(list1)
print(s1)
print(type(list1))
print(type(s1))

s1 = {1, 2, 3, 4, 5, 6, 2} # O 2 não aparece
s1.add(7) # Adiciona um item
s1.add(1) # Ignora pois já exite o 1
s1.update([8, 9, 10]) # Adiciona varios itens

print(s1)

s1.remove(10) # Remove o número 10
s1.discard(9) # Discarta o 9

# O discard não retorna erro caso você tente remover um número que não existe, o remove retorna erro