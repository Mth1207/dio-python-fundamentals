"""
Um set é uma coleção que não possui objetos repetidos.
Usado para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável.
OBS: Set nao retorna de forma ordenada
"""
####################################################

# EXEMPLO SET
numeros = set([1, 2, 3, 1, 2, 3, 4]) 
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("palio", "gol", "celta", "palio"))
print(carros)

# Utilizando set sem o construtor
linguagens = {"python", "java", "python"}
print(linguagens)

####################################################

# Quando precisar acessar os valores do set, precisará convertê-los para uma lista
# ex:
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])

####################################################

# Iterando com for
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)
    
####################################################
    
# Iterando com enumerate
for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")    

####################################################

#  MÉTODOS ↓

# Método union - une os dois conjuntos
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

####################################################

# Método intersection - une a intersecção entre dois conjuntos, no exemplo abaixo seriam o 2 e 3
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.intersection(conjunto_b)
print(conjunto_c)

####################################################

# Método difference - tudo que há em um conjunto, mas não existe no outro
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

dif_a_com_b = conjunto_a.difference(conjunto_b) # 1 tem no A mas não tem no B
print(dif_a_com_b)
dif_b_com_a = conjunto_b.difference(conjunto_a) # 4 tem no B mas não tem no A
print(dif_b_com_a)

####################################################

# Método symetric_difference - pega todos os elementos que não estao na intersecção
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

diferenca = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca)

####################################################

"""
EXPLICAÇÃO issubset E issuperset
Pense assim:
issubset: Imagine que você tem uma lista de coisas que você tem e outra lista maior que contém tudo o que está disponível em uma loja. 
Se tudo o que você tem está nessa loja, então sua lista é um subconjunto (issubset) do que está disponível na loja.

Exemplo:

Sua lista: {1, 2, 3}
Loja: {1, 2, 3, 4, 5}
Tudo o que você tem está na loja, então sua_lista.issubset(loja) é True.

issuperset: Agora, imagine que você tem uma lista e quer saber se ela contém tudo o que está em outra lista menor. 
Se sua lista tem tudo o que está na lista menor, então sua lista é um superconjunto (issuperset) da lista menor.

Exemplo:

Sua lista: {1, 2, 3, 4, 5}
Outra lista menor: {1, 2, 3}
Sua lista contém tudo da lista menor, então sua_lista.issuperset(outra_lista) é True.

Resumindo:
issubset: Verifica se tudo do menor está no maior.
issuperset: Verifica se tudo do menor está no maior (mas agora, você está olhando do ponto de vista do maior).
"""

####################################################

# Método issubset - A.issubset(B): Verifica se A é um subconjunto de B (ou seja, todos os elementos de A estão em B).
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) # True 1, 2 e 3 estão dentro de B, pois são equivalentes
print(conjunto_b.issubset(conjunto_a)) # False 4, 5 e 6 não pertencem em A.

####################################################

# Método issuperset - A.issuperset(B): Verifica se A é um superconjunto de B (ou seja, todos os elementos de B estão em A).
print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True

####################################################

# Método isdisjoint - é usado para verificar se dois conjuntos possuem elementos em comum. Caso possuir retornará True senão False
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))
print(conjunto_b.isdisjoint(conjunto_c))

####################################################

# Métodos add - caso elemento não exista no conjunto, será adicionado, caso elemento já exista, será ignorado e não será adicionado.
sorteio = {1, 23}

sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

####################################################

# Método clear - limpará todo o set
print(sorteio)
sorteio.clear()
print(sorteio)

####################################################

# Método copy - Fará uma cópia do set, mas em outro endereço de memória.
sorteio = {1, 23}

sorteio.copy()
print(sorteio)

####################################################

# Método discard - descarta valores que são passados como argumentos. Caso passe um valor que não exista no set, não terá problema, pois não tem como eliminar algo que não exista.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0,}

print(numeros)
numeros.discard(1)
print(numeros)
numeros.discard(45)
print(numeros)

####################################################

# Método pop - elimina os elementos do set de acordo com o primeiro elemento existente. FIFO
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros.pop())
print(numeros)

####################################################

# Método remove - é semelhante ao discard, porém se passar um valor que não existe como parâmetro, será gerado um KeyError.
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)
print(numeros.remove(0))
print(numeros)

####################################################

# Função len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))

####################################################

# in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)
print(10 in numeros)

####################################################