nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
rendaM = float(input("Digite sua renda mensal: R$"))
valEmpr = float(input("Digite o valor do empréstimo desejado: R$"))
nParc = int(input("Digite a quant. de parcelas (3 a 24): "))


#Funções do empréstimo
def pode_aprovar(idade, renda, valor):
    aprovado = 0
    if idade >=18 and valor<renda*20:
        aprovado = 1
    return aprovado
aprovado = pode_aprovar(idade,rendaM, valEmpr)


def definir_taxas(parcelas):
    taxa = 0
    if parcelas>3 or parcelas<24:
        if parcelas<=6:
            taxa = 0.05
        elif parcelas<=12:
            taxa = 0.08
        else:
            taxa = 0.1
    return taxa
taxa = definir_taxas(nParc)


def calcular_parcela(valor, taxa, parcelas):
    if(taxa):
        pmt = valor * (taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)
    else: pmt = 0
    return pmt
pmt = calcular_parcela(valEmpr, taxa, nParc)


def calcular_total(parcela, parcelas):
    total = parcela * parcelas
    return total
total = calcular_total(pmt, nParc)


def calcular_juros(total, valor):
    juros = total - valor
    return juros
juros = calcular_juros(total, valEmpr)


#Empréstimo
if(aprovado):
    if(taxa):
        print("Empréstimo aprovado!")
        print(f"Nome do cliente: {nome} - Valor Financiado: R${valEmpr:.2f}")
        print(f"Taxa de juros: {taxa*100}% - Valor da Parcela: R${pmt:.2f}")
        print(f"Valor total: R${total:.2f} - Valor do total dos juros: {juros:.2f}")
    else: print("Número de parcelas inválido")
else: print("Empréstimo negado")
