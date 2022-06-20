'''
# Exemplo 5 - Fatorial de um número
> Crie um programa que recebe um número e imprime o seu fatorial

# Método 5Q's para montar o algorítimo:
Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreeender completamente o problema)

1. Quais são os dados de entrada necessários?
Número digitado pelo usuário.

2. O que devo fazer com estes dados?
Devo calcular o fatorial do número escolhido e o exibir na tela.

3. Quais são as restrições deste problema?
O número deve ser um valor positivo e inteiro.

4. Qual é o resultado esperado?
Espera-se que o fatorial do número escolhido seja exibido.

5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
  fatorial = fatorial * numero
print(fatorial)
'''

numero = int(input('Digite um número'))
if numero > 0:
  fatorial = 1
  for item in range(1,numero +1):
    fatorial = fatorial * item
print (fatorial)
