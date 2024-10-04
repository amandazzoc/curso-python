# Set (listas)
  # Similar a listas
  # Evita itens duplicados
  # Não utiliza index

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1) # Converte para sets
num2 = set(list2)

print(num1 | num2) # Union
print(num1 - num2) # Difference
print(num1 ^ num2) # Symmetric Difference - retira os duplicados nas duas listas
print(num1 & num2) # And

print(len(num1))
print(num1[0]) # Erro pois o index perdeu os index
