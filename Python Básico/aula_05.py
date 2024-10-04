mensagem = '      eu adoro comida Caseira'

print(mensagem.lower()) # letra minúscula
print(mensagem.upper()) # letra maiuscula
print(mensagem.capitalize()) # primeira letra em maiusculo
print(mensagem.find('c')) # mostra o index da letra na string
print(mensagem.find('adoro')) # mostra o index inicio da palavra
print(mensagem.find('y')) # mostra -1 pois não encontrou
print(mensagem.replace('a', 'e')) # troca as letras a por e
print(mensagem.replace('Caseira', 'Feita em casa')) # troca a palavra caseira por feita em casa
print(mensagem.strip()) # remove os espaços antes do primeiro caractere
