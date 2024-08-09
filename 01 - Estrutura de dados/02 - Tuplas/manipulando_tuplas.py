""""
Tuplas são imutáveis

"""

####################################################

# Criando tuplas
frutas = ("laranja", "pera", "uva",)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)   # Quando utilizar tupla, no final sempre colocar uma vírgula.
print(pais)

####################################################

# Acessando valores da tupla
frutas = ("maçã", "laranja", "uva", "pera",)
print(frutas[0])
print(frutas[2])

# Acessando valores negativos
print(frutas[-1])
print(frutas[-3])

####################################################

# Tuplas aninhadas.
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

####################################################

# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

####################################################

# Iterando tuplas
carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)
    
# Utilizando enumerate
for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")
    
####################################################

# MÉTODOS PARA TUPLAS

# Método count
cores = ("vermelho", "azul", "verde", "azul",)

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

####################################################

# Método index
linguagens = ("python", "js", "c", "java", "csharp")

print(linguagens.index("java"))
print(linguagens.index("python"))

####################################################

# Função len
linguagens = ("python", "js", "c", "java", "csharp")

print(len(linguagens))

####################################################
