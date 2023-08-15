from paciente import  Registrar

nome = input('digite seu nome: ')
idade = int(input('digite sua idade: '))
cpf = int(input('digite seu cpf (somente números): '))
email = input('digite seu email: ')
Paciente = Registrar(nome, idade, cpf, email)
print(f"seu nome é", nome,"você possui",idade,"anos, seu cpf é",cpf,"seu email é:",email,"confirma ?")
confirma = input("[S/N]: ").lower
if confirma == "s":
    print('bem vindo')
elif confirma == "n":
    print('reinicinado cadastro...')
else: 
    print('resposta inválida')
