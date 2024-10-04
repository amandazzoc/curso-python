#Função que soma vários números

def soma(*numeros): # o * apresenta que vários números podem entrar la
  resultado = 0
  for num in numeros:
    resultado += num
  return resultado

x = soma (2,3,4,7,4)
print(x)
