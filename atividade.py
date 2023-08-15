nome = input('digite seu nome: ')
salario = float(input('digite seu salário:R$'))
if salario >= 1200 and salario < 2400: 
    print(nome ,'você recebeu um aumento de 15%, recebendo agora :R$',salario*1.15)
elif salario >=2400:
    print('nome,você recebeu um aumento de 7%, recebendo agora :R$',salario*1.07)
else: 
    print('nenhum aumento para', nome)