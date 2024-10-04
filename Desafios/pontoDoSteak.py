# Desafio com if, Elif, Else

'''
Criar um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. O usuario devera fornecer a temperatura.

Temperaturas - cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (bem passa)
'''

try:
  temperatura = int(input('Digite a temperatura da carne em °C: '))
except ValueError:
  print('Favor digitar um valor em numeros')

if temperatura < 48:
  print('Cozinhar por mais alguns minutos')
elif 54 > temperatura >= 48:
  print('Selada')
elif 60 > temperatura >= 54:
  print('Ao ponto para o mal')
elif 65 > temperatura >= 60:
  print('Ao Ponto')
elif 71 > temperatura >= 65:
  print('Ao ponto para bem')
else:
  print('Bem passada')

