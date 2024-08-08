nome = "Matheus"
idade = 29
profissao = "Programador"
linguagem = "Python"
saldo = 45.532


# Dicionário
pessoa = {"nome": "Matheus", "idade": 29, "profissao": "Programador 1", "linguagem": "Python"} 


# Old Style
print("Olá, meu nome é %s. Tenho %d anos de idade, trabalho como %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem))

########################################

# Método format
print("Olá, meu nome é {}. Tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
print("Olá, meu nome é {3}. Tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
print("Olá, meu nome é {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format(nome = nome, idade = idade, profissao = profissao, linguagem = linguagem))
print("Olá, meu nome é {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.".format( **pessoa))

########################################

# Método f-strings
print(f"Olá, meu nome é {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
print(f"Nome: {nome}, Idade: {idade}, Saldo: {saldo:.2f}")

########################################

PI = 3.14159

print(f"valor de PI: {PI: .2f}")
print(f"valor de PI: {PI: 10.2f}")