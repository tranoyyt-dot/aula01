from datetime import date

def calcular_idade(data_nascimento):
    hoje = date.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

ano = int(input("Digite o seu ano de nascimento: "))
mes = int(input("Digite o seu mês de nascimento: "))
dia = int(input("Digite o seu dia de nascimento: "))

data_nascimento_utilizador = date(ano, mes, dia)
idade_calculada = calcular_idade(data_nascimento_utilizador)

print(f"A sua idade é: {idade_calculada} anos.")