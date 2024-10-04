from datetime import datetime
# Criar a classe
class Funcionarios:
  def __init__(self, nome, sobrenome, data_nascimento, ano_nascimento): # Faz um construtor # Self é o objeto.argumento, sem precisar referenciar o objeto
    self.nome = nome
    self.sobrenome = sobrenome
    self.data_nascimento = data_nascimento
    self.ano_nascimento = ano_nascimento

  def nome_completo(self):
    return self.nome + ' ' + self.sobrenome

  def idade_funcionario(self):
    ano_atual = datetime.now().year
    self.ano_nascimento = int(ano_atual - self.ano_nascimento)
    return self.ano_nascimento


# Criar o objeto
usuario1 = Funcionarios('Elena', 'Cabral', '12/01/1992', 1992)
usuario2 = Funcionarios('Carol', 'Silva', '15/10/2000', 2000)

print(usuario1.nome)
print(usuario2.nome)
print(usuario1.nome_completo())
print(usuario2.nome_completo())
print(Funcionarios.nome_completo(usuario1)) # Mesma coisa que o de cima
print(Funcionarios.idade_funcionario(usuario1))