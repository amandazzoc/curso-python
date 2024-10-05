# Calculo de IMC - Índice de Massa Corporal

'''
Qual é a sua Altura em cm:
Qual é o seu peso em kg
'''

# MENOR QUE 18,5    MAGREZA
# ENTRE 18,5 E 24,9 NORMAL
# ENTRE 25,0 E 29,9 SOBREPESO
# ENTRE 30,0 E 39,9 OBESIDADE
# MAIOR QUE 40,0    OBESIDADE GRAVE

peso = float(input('Qual é o seu peso e kg? '))
altura = float(input('Qual é a sua altura em cm? '))

altura_m = altura / 100
imc = peso / (altura_m**2)

if imc < 18.5:
    print('MAGREZA')
elif 24.9 <= imc >= 18.5:
    print('NORMAL')
elif 29.9 <= imc >= 25:
    print('SOBREPESO')
elif 39.9 <= imc >= 30:
    print('OBESIDADE')
else:
    print('OBESIDADE GRAVE')