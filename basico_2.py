# ========================================= EXERCÍCIO 1 =========================================

# nome = input('Digite seu nome: ')

# sobrenome = input('Digite seu sobrenome: ')

# idade = int(input('Digite sua idade: '))

# ano_nascimento = input('Digite o ano de nascimento: ')

# altura_cm = input('Digite sua altura em centímetros: ')

# maior_idade = idade >= 18

# print('Nome: ', nome)

# print('Sobrenome: ',sobrenome)

# print('Idade: ', idade)

# print('Ano de nascimento: ', ano_nascimento)

# print('É maior de idade? ', maior_idade)

# print('Altura em centímetros: ', altura_cm)

# print(f' Seu nome é {nome} {sobrenome}, possui {idade} anos. É nascido em {ano_nascimento} e mede {altura_cm} centímetros.')

# ================================================================================================

# soma = 10+2
# print(soma)

# exponenciacao = 10 ** 2
# print(exponenciacao)

# modulo = 10 % 3 
# print(modulo) # módulo é o resto da divisão

# divisao = 10 / 3
# divisao = round(divisao, 2)
# print(divisao)

# divisao_inteira = 10 // 3
# print(divisao_inteira) # divisão inteira é a divisão inteira


# print(10 % 2 ==0) #verifica se um número é par


# conta_1 = (1 + 1) ** (5 + 5)

# print(conta_1)


# Cálculo de IMC
peso = input('Digite seu peso: ')

altura = input('Digite sua altura em centímetros: ')

altura_normalizada = float(altura) / 100

imc = round(float(peso) / float(altura_normalizada * altura_normalizada), 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc >= 18.5 and imc <= 24.9:
    classificacao = "Peso normal"
elif imc >= 25 and imc <= 29.9:
    classificacao = "Sobrepeso"
elif imc >= 30 and imc <= 34.9:
    classificacao = "Obesidade grau I"
elif imc >= 35 and imc <= 39.9:
    classificacao = "Obesidade grau II"
else:
    classificacao = "Obesidade grau III"

print(f'Seu IMC é de: {imc} e sua classificação é: {classificacao}')