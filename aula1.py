'''
Isso é um Docstring
'''

print("Olá Mundo python")

# Tipos de dados
# Python possui tipagem dinâmica e forte.
# int
idade = 20
# float
altura = 1.75
# str
nome = "João"
# bool
maior_de_idade = True

print(nome, "possui", idade, "anos e", altura, "de altura")

print("Daniel \"Mota")


idade_daniel = 42

idade_tati = 41
print("A diferença de idade entre Daniel e Tati é de", idade_daniel - idade_tati, "ano(s)")

print(type(idade_daniel))

validacao = idade_daniel > idade_tati

print(validacao)

print(type(validacao))

print(type(10 + 11.3))

print('a' + '1')

#Coerção de tipos
print(int('1')) # Aqui digitou-se um string e o python converteu para int

print(float('1.2')) # Aqui digitou-se um string e o python converteu para float

print(bool(1))

import re

# Limpando o input que aceita letras e outros caracteres
numero = input("Digite sua idade: ")

numero_limpo = re.sub(r'[^0-9]', '', numero)

resultado = int(numero_limpo)

print(nome , 'possui', resultado, 'anos')
