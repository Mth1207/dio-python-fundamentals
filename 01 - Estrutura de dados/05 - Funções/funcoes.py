def exibir_mensagem():
    print("Olá mundo!")
    
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo{nome}")
    
def exibir_mensagem_3(nome=" Anonimo"):
    print(f"Seja bem vindo{nome}")
    
exibir_mensagem()
exibir_mensagem_2(nome=" Matheus")
exibir_mensagem_3()
exibir_mensagem_3(nome=" Chappie")

####################################################

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    
    return antecessor, sucessor

def func_3():
    print("Olá Mundo!")


print(calcular_total([10, 20, 34])) # 64
print(retorna_antecessor_e_sucessor(10)) # 9, 11
print(func_3()) # None

####################################################

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")
    
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

####################################################

# *args = recebe tupla    /// **kwargs = recebe um dicionário

####################################################

def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"\n{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)
    
exibir_poema("Sexta, 26 ago 22", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)

####################################################
"""
---------------
SINTAXE DE PARÂMETROS

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
       .........     ..........     ..........
        |                                 |
        |       Positional or keyword     |  
        |                                 |
         -- Positional only               - keyword only

---------------
"""

####################################################

# Positional Only
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Esta chamada é válida, seguindo as orientações do Positional only

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # chamada inválida!

####################################################

# Keyword Only
def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Válida porque queremos que sejam passados as palavras como parâmetros

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Inválido!!

####################################################

# Keyword and positional only
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # chamada inválida!

####################################################

# OBJETOS DE PRIMEIRA CLASSE
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação é = {resultado}")
    
exibir_resultado(10, 10, somar)
exibir_resultado(10, 10, subtrair)

op = somar
print(op(1, 23))

####################################################

# ESCOPO DE VARIAVEIS
#Exemplo:
salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(500))

#####

def salario_bonus_2(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(2)
    print(f"lista aux = {lista_aux}")
    
    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus_2(500, lista)
print(salario_com_bonus)
print(lista)

####################################################

