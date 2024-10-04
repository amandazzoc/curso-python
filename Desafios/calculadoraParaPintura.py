# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para pintar
uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta
'''

altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))
rendimento = int(input('Qual o rendimento da lata? '))

def calcula_latas():
  num_latas = ((altura * largura) / rendimento)
  print(f'Você precisa de {num_latas} latas de tinta')

calcula_latas()