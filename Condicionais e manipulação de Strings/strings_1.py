curso = "pYthon"

print(curso.upper())
print(curso.lower())
print(curso.title()) # primeira letra de cada palavra em maiúsculo

curso = "   teste "

print(curso.strip() + ".") # remove espaços em branco da direita/esquerda
print(curso.lstrip() + ".") # remove espaços em branco na esquerda
print(curso.rstrip() + ".") # remove espaços em branco na direita

curso = "Python"

# coloca a palavra no centro, primeiro argumento é a quantidade de caracteres da palavra e o segundo argumento é o que substituirá os novos espaços em branco
print(curso.center(10, "#")) 

print(".".join(curso)) # separa cada caracter com o que foi utilizado no primeiro argumento

