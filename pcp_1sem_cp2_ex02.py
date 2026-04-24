# Inserção de dados
a = float(input("Insira o valor de A: "))
b = float(input("Insira o valor de B: "))
c = float(input("Insira o valor de C: "))
# Organização
lados = sorted([a, b, c], reverse=True)
A, B, C = lados
# Condições com prints
if A >= B + C:
    print("Não é possível formar triângulo")
else:
    if A == B == C:
        print("TRIÂNGULO EQUILÁTERO")
    else:
        if A**2 == B**2 + C**2:
            print("TRIÂNGULO RETÂNGULO")
        elif A**2 > B**2 + C**2:
            print("TRIÂNGULO OBTUSÂNGULO")
        elif A**2 < B**2 + C**2:
            print("TRIÂNGULO ACUTÂNGULO")

        if A == B or B == C or A == C:
            print("TRIÂNGULO ISÓSCELES")