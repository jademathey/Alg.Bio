
#1
def calcula_imc(peso, altura):
    return peso / (altura ** 2)

def resultado_imc(imc):
    if imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else: 
        return "Obesidade"
    
nome = input("Nome: ")
sexo = input("Sexo (M/F): ")
peso = float(input("Peso(kg): "))
altura = float(input("Altura (m): "))

imc = calcula_imc(peso, altura)
situacao = resultado_imc(imc)

print(f"\n Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Peso> {peso:.2f} kg")
print(f"Altura: {altura:.2f} m")
print(f"Situação : {situacao:.2f}")

#2 Criar funções a) ordenar lista de números em ordem crescente
def ordenar_lista(lista):
    return sorted(lista)

numeros = [9, 2, 7, 1, 5]
print("Lista ordenada: ", ordenar_lista(numeros))


#2 b) Função com entradas (nome, RA, média final) e saída da situação

def avalia_aluno(nome, ra, media):
    if media >= 6:
        situacao = "Aprovado"

