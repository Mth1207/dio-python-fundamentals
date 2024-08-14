# CRIANDO DICIONARIOS
pessoa = {"nome":"Matheus", "idade":29}
print(pessoa)

pessoa = dict(nome="Matheus", idade=29)
print(pessoa)

pessoa["telefone"] = "3333-1234"
print(pessoa)

####################################################

# ACESSANDO DICIONARIOS
pessoa = {'nome': 'Matheus', 'idade': 29, 'telefone': '3333-1234'}

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

pessoa["nome"] = "Maria"
pessoa["idade"] = 18
pessoa["telefone"] = "9988-1781"

print(pessoa)

####################################################

# DICIONÁRIOS ANINHADOS
contatos = {
    "guilherme@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Gionvanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print(contatos["giovana@gmail.com"]["telefone"])

####################################################

# ITERANDO SOBRE DICIONÁRIOS
for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, valor)

####################################################

# Método clear
contatos = {
    "guilherme@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Gionvanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

contatos.clear()
print(contatos)

####################################################

# Método copy
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

copia = contatos.copy()
copia["matheus@gmail.com"] = {"nome":"Mat"}
print(contatos["matheus@gmail.com"])
print(copia)

####################################################

# Método fromkeys - cria chaves sem valores ou com algum valor padrão

# Dicionarios que ainda não existem
print(dict.fromkeys(["nome","telefone"]))  # criando chaves sem valores, "nome" : None, "telefone": None

print(dict.fromkeys(["nome", "telefone"], "vazio")) # criando chaves com valor padrão "vazio", "nome": "vazio", "telefone": "vazio"

# Dicionarios existentes ficará a sintaxe: ↓
print(contatos.fromkeys(["nome", "telefone"]))

####################################################


print("\nGET PARA BAIXO\n")

# Método get
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

# contatos["chave"]

print(contatos.get("chave")) # quando não encontra a chave retorna None
print(contatos.get("chave", {})) # Passa valor default, caso não encontrar a chave, retornará um valor default, nesse caso {}
print(contatos.get("matheus@gmail.com", {})) # Se a chave for encontrada retorna todo o dicionário

####################################################

# Método items
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

print(contatos.items())

####################################################

# Método keys
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

print(contatos.keys())

novo_dicionario = {"a": 100, 1 : "teste", "b" : "python"}
print(novo_dicionario.keys())

####################################################

# Método pop
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

print(contatos)

print(contatos.pop("matheus@gmail.com")) # Removeu a chave "matheus@gmail.com"
print(contatos.pop("matheus@gmail.com", {})) # Caso não encontre a chave, retornará um valor default, nesse caso {}

####################################################

print("\nPOP ITEM PARA BAIXO: ↓\n")

# Método popitem
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

print(contatos.popitem())

####################################################


print("\nSET DEFAULT PARA BAIXO: ↓\n")

# Método setdefault
contatos = {"nome": "Matheus", "telefone": "3333-2221"}

contatos.setdefault("nome", "Giovanna") # não substitui o valor original
print(contatos)

contatos.setdefault("idade", 28) # nesse caso como idade não faz parte do dicionario, idade sera adicionado.
print(contatos)

####################################################

print('\nUPDATE PARA BAIXO: ↓\n')

# Método update
contatos = {
    "matheus@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"}
}

contatos.update({"matheus@gmail.com": {"nome" : "Mat"}})
print(contatos)

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-8181"}})
print(contatos)

####################################################

print('\nVALUES PARA BAIXO: ↓\n')

# Método value - retorna todos os valores sem retornar as chaves.
contatos = {
    "guilherme@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Gionvanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

teste = contatos.values()
print(teste)

####################################################

print('\nMÉTODO IN PARA BAIXO: ↓\n')

# Método in - forma elegante de verificar se uma chave existe ou não
contatos = {
    "guilherme@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Gionvanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

print("guilherme@gmail.com" in  contatos) # True
print("megui@gmail.com" in  contatos) # False
print("idade" in  contatos["guilherme@gmail.com"]) # False
print("telefone" in  contatos["giovana@gmail.com"]) # True

####################################################

print("\nMÉTODO DEL PARA BAIXO: ↓\n")

# Método del
contatos = {
    "guilherme@gmail.com": {"nome": "Matheus", "telefone": "3333-2221"},
    "giovana@gmail.com": {"nome": "Gionvanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

print(contatos)

####################################################
