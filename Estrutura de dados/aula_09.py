from array import array

# Array (Matriz) para grande quantidades de itens 

letras = ['a', 'b', 'c', 'd']
numero_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

print(letras)
print(numero_i)
print(numeros_f)

print()

letras = array('u', ['a', 'b', 'c', 'd']) # Se a lista for de strings, é usado o u
numero_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

print(letras)
print(numero_i)
print(numeros_f)