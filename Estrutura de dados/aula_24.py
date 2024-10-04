from sys import getsizeof

# Generator Expressions
  # Uma forma mais rápida para Listas, dicionário e etc
  # Menos memória alocada
  # Valores em bytes

numeros = [x * 10 for x in range(100000)]
print(type(numeros))
print(getsizeof(numeros))

numeros = (x * 10 for x in range(100000))
print(type(numeros))
print(getsizeof(numeros))