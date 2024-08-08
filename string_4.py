nome = "Matheus"
menu = " MENU "
rodape = ""
mensagem_final = "Obrigado por usar nosso sistema."

mensagem = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)

print(f"""
{menu.center(50, "#")}

1 - Depositar
2 - Sacar
0 - Sair

{rodape.center(50, "#")}
      
{mensagem_final.center(50)}
    
      """)