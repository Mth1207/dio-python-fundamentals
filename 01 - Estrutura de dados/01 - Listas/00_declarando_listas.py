frutas = ["laranja", "maça", 'uva']
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)
print(letras[:2]) # ["p", "y"]
print(letras[0:3:2]) # ["p", "t"]
print(letras[::]) # ["p", "y", "t", "h", "o", "n"]
print(letras[::-1]) # ["n", "o", "h", "t", "y", "p"]
 
numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)
    
for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")
    
####################################################
    
# FILTRO VERSÃO 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)    

####################################################

# MODIFICANDO VALORES VERSÃO 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

####################################################

# FILTRO VERSÃO 2 usando list comprehension
numeros_v2 = [2, 50, 22, 3, 9, 68, 34]
pares_v2 = [numero for numero in numeros if numero % 2 == 0]
print(pares_v2)

####################################################

# MODIFICANDO VALORES VERSÃO 2

pares_v2 = [numero ** 2 for numero in numeros_v2]
print(pares_v2)

