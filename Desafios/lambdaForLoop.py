quadrado = lambda num: num ** 2

numeros = [1,2,3,4,5,6,7,8,9,10]
resultados = []
for i in numeros:
  resultados.append(quadrado(i))

print(resultados)