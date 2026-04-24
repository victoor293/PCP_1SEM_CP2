# Solicitação de informações
nome = input('Insira o seu nome: ')

print('- Cargos -')
print('1 - Gerente')
print('2 - Analista')
print('3 - Assistente')
print('4 - Estagiário')
print('Insira o número do seu cargo: ')
opcao = input()

if opcao == '1':
    cargo = 'Gerente'
elif opcao == '2':
    cargo = 'Analista'
elif opcao == '3':
    cargo = 'Assistente'
elif opcao == '4':
    cargo = 'Estagiário'
else:
    print('Cargo inválido')

print('Cargo definido:', cargo)

salario_base = float(input('Insira seu salário mensal: '))
total_hrs_ext = int(input('Insira a quantidade de horas extras trabalhadas no mês: '))
total_faltas = int(input('Insira a sua quantidade de faltas no mês: '))
bonus = input('Você obteve bônus por desempenho nesse mês? (s/n) ')

if bonus == 's' or bonus == 'S':
    recebeu_bonus = True
elif bonus == 'n' or bonus == 'N':
    recebeu_bonus = False
else:
    print('Resposta inválida')

def calcular_horas_extras(salario_base, total_hrs_ext):
    return (salario_base * 0.015) * total_hrs_ext

def calcular_descontos_faltas(salario_base, total_faltas):
    return (salario_base * 0.02) * total_faltas

def calcular_bonus(cargo, recebeu_bonus):
    if cargo == 'Gerente' and recebeu_bonus == True:
        return 1000
    elif cargo == 'Analista' and recebeu_bonus == True:
        return 500
    elif cargo == 'Assistente' and recebeu_bonus == True:
        return 300
    elif cargo == 'Estagiário' and recebeu_bonus == True:
        return 100
    else:
        return 0

salario_bruto = salario_base + calcular_horas_extras(salario_base, total_hrs_ext) + calcular_bonus(cargo, recebeu_bonus)
acrescimos = calcular_horas_extras(salario_base, total_hrs_ext) + calcular_bonus(cargo, recebeu_bonus)
total_descontos = calcular_descontos_faltas(salario_base, total_faltas)
salario_final = salario_bruto - total_descontos

# Exibição

print(f'O seu salário bruto é de: R$ {salario_bruto:.2f}')
print(f'O total de acréscimos foi de: R$ {acrescimos:.2f}')
print(f'O total de descontos foi de: R$ {total_descontos:.2f}')
print(f'O seu salário final é de: R$ {salario_final:.2f}!')