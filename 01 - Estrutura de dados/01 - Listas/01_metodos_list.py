# MÉTODO APPEND
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)

####################################################

# MÉTODO CLEAR
lista = [1, 'Python', [40, 30, 20]]

print(lista)
lista.clear()
print(lista)

####################################################

# MÉTODO COPY - Faz uma cópia da lista, ficando em endereços diferentes (Ver parte do id())
lista = [1, 'Python', [40, 30, 20]]

l2 = lista.copy()

print(lista)

print(id(l2), id(lista))
    
    # é possível fazer alterações em "l2" sem alterar "lista" ↓
l2[0] = 2
print(f"""
      lista = {lista} 
      l2    = {l2}
      """)

####################################################

# MÉTODO COUNT - faz a contagem dos objetos dentro da lista
cores = ["vermelho", "azul", "verde", "azul"]

print(f"""
    cores = {cores}
      
    vermelho = {cores.count("vermelho")}x
    verde = {cores.count("verde")}x
    azul = {cores.count("azul")}x
""")

####################################################

# MÉTODO EXTEND - juntará o conteúdo de uma lista ao final de outra lista ja existente. OBS: não exclui valores duplicados.
linguagens = ["Python", "JS", "C"]

print(linguagens)

linguagens.extend(["Java", "CSharp"])

print(linguagens) 

####################################################

# MÉTODO INDEX - mostra em qual índice o conteúdo informado está. OBS: pegará a primeira ocorrência, caso duplicado pegará o primeiro.
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))
print(linguagens.index("python"))

####################################################

# MÉTODO POP - remove o último elemento da lista ou qual for passado no argumento.

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0) # retira "python" da lista
print(linguagens)

####################################################

# MÉTODO REMOVE - remove o elemento passado como argumento da lista. OBS: caso tenha elementos duplicados, removerá somente o primeiro.
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("c")
print(linguagens)

####################################################

# MÉTODO REVERSE - inverte os elementos da lista de trás para frente.
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()
print(linguagens)

####################################################

# MÉTODO SORT - faz ordenação da lista em ordem alfabética
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens)

####################################################

# FUNÇÃO LEN - verifica o tamanho da lista (função built-in)
linguagens = ["python", "js", "c", "java", "csharp"]
print(len(linguagens))

####################################################

# FUNÇÃO SORTED - ordenar iteráveis (função built-in)
linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x)))

linguagens = ["python", "js", "c", "java", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))

####################################################