# Inserção inicial de dados
cod_estado_carga = int(input("Insira o código do estado de origem da carga: "))
# Condição para continuação do programa
while cod_estado_carga < 1 or cod_estado_carga > 5:
    print('Código inválido')
    cod_estado_carga = int(input("Insira o código do estado de origem da carga: "))
# Inserção de outros dados
peso_carga = float(input('Insira o peso da carga em toneladas: '))

cod_carga = int(input('Insira o código da carga: '))
# Condição para continuação do programa
while cod_carga < 10 or cod_carga > 40:
    print('Código inválido')
    cod_carga = int(input('Insira o código da carga: '))
# Fórmula para eficiência nos prints
peso_carga_conv = peso_carga * 1000
# Condições para preços
if 10 <= cod_carga <= 20:
    preco_carga = peso_carga_conv * 100
elif 21 <= cod_carga <= 30:
    preco_carga = peso_carga_conv * 250
else:
    preco_carga = peso_carga_conv * 340
# Condições para impostos
if cod_estado_carga == 1:
    imposto = 0.35
elif cod_estado_carga == 2:
    imposto = 0.25
elif cod_estado_carga == 3:
    imposto = 0.15
elif cod_estado_carga == 4:
    imposto = 0.05
else:
    imposto = 0
# Fórmulas para eficiência nos prints
imposto_cobrado = preco_carga * imposto
valor_total = preco_carga + imposto_cobrado
# Exibição final
print(f'O peso da carga em kg é de: {peso_carga_conv:.2f}kg')
print(f'O preço da carga é de: R${preco_carga:.2f}')
print(f'O valor do imposto cobrado é de: R${imposto_cobrado:.2f}')
print(f'O valor total a ser transportado é de: R${valor_total:.2f}')