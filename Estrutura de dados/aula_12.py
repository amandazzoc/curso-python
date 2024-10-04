# Set (listas)
  # Similar a listas
  # Evita itens duplicados
  # Não utiliza index

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.union(set2) # Une o set1 e o set2
set5 = set1.difference(set3) # Diferença entre os Sets
set6 = set1.intersection(set2) # intersecção
set7 = set1.symmetric_difference(set3) # diferença simetrica

print(set4)
print(set5)
print(set6)
print(set7)