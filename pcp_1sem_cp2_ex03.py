## Uma instituição de ensino avalia seus alunos ao longo do semestre com base em diferentes atividades.

# Solicitar as notas - Entrada de Dados

CP1 = float(input("Digite sua nota do CheckPoint 1 (0 a 10): "))
CP2 = float(input("Digite sua nota do CheckPoint 2 (0 a 10): "))
CP3 = float(input("Digite sua nota do CheckPoint 3 (0 a 10): "))
SP1 = float(input("Digite sua nota do Sprint 1 (0 a 10): "))
SP2 = float(input("Digite sua nota do Sprint 2 (0 a 10): "))
GS = float(input("Digite sua nota do Global Solution (0 a 10): "))

# Identificar a menor nota entre os Checkpoints

menor = CP1

if CP2 < menor:
    menor = CP2

if CP3 < menor:
    menor = CP3

# Composição da Média com os seguintes pesos:

# 40% ou 0.4 → média dos 2 maiores Checkpoints + 2 Sprints
# 60% ou 0.6 → nota da Global Solution
# 40% ou 0.4 → média do 1º semestre

# Cálculo da média

soma_cp = CP1 + CP2 + CP3 - menor
media_componentes = (soma_cp + SP1 + SP2) / 4

# Média do semestre (sem peso)
media = (media_componentes * 0.4) + (GS * 0.6)

# Média de peso
media_peso = media * 0.4

print(f"A média do semestre é de: {media}.")
print(f"A média do semestre com peso é de: {media_peso}.")

if media >= 6:
   print("Situação do aluno: Aprovado(a).")
elif media >= 4:
   print("Situação do aluno: Recuperação.")
else:
   print("Situação do aluno: Reprovado.")
