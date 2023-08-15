# uma senha usa letras maiusculas e minusculas
# utiliza simbolos e espaços

"""
Security = chave
5ecurt1ty = senha
"""

chave = input("digite a base da sua senha: ")
senha = ""
for letra in chave:
    if letra in "Aa":
        senha = senha + "10"
    elif letra in "Bb":
        senha = senha + "11"
    elif letra in "Cc":
        senha = senha + "12"
    elif letra in "Dd":
        senha = senha + "13"
    elif letra in "Ee":
        senha = senha + "14"
    elif letra in "Ff":
        senha = senha + "15"
    elif letra in "Rr":
        senha = senha + "%"
    elif letra in "Ff":
        senha = senha + "$"
    elif letra in "Ss":
        senha = senha + "&"
    elif letra in "Uu":
        senha = senha + "!"
    else:
        senha = senha + letra
print(senha)
