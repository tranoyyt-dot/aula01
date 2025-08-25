idade = int(input('infome sua idade: '))
if(idade <= 12):
    print('\n Usuario Criança')
elif(idade > 12 and idade <= 17):
    print('\n Usuario Adolescente')
elif(idade >= 18 and idade <= 59):
    print('\n Usuario Adulto')
elif(idade > 59):
    print('\n Usuario Idoso')
else:
    print('\n Erro-')