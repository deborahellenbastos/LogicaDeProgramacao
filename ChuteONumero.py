'''
#Projeto - Chute o número Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até acertar o valor gerado. O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no programa.

Método 5Q's para montar o algorítimo:
Analise criticamente o problema e descubra: (Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreeender completamente o problema)

Quais são os dados de entrada necessários?
gerar um valor aleatorio de 1 a 10 chute do usuario

O que devo fazer com ?
comparar os numeros e mostrar na tela informando se foi maior, menor ou igual.

Quais são as restrições deste problema?
um valor de 1 a 10

Qual é o resultado esperado?
o resultado esperado é o programa comparar os numeros e mostrar na tela informando se foi maior, menor ou igual.

Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

input valor_aleatorio de 1 a 10
chute
if chute > valor_aleatorio
print "Chute maior que o número gerado"
if chute < valor_aleatorio
print "Chute menor que o número gerado"
if chute = valor_aleatorio
print "Você acertou"
'''

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute maior que o número gerado')
  elif chute < valor_aleatorio:
    print('Chute menor que o número gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!')
