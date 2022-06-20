'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima. Levando em consideração que se a pessoa estiver abaixo da velocidade máxima seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir: "levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima, exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima, exiba: "levou multa gravíssima".

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz alta e peça mais informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
- velocidade recebida pelo usuário
- velocidade de 80km para comparação

2. O que devo fazer com estes dados?
Comparar a velocidade do usuário com a máxima permitida e informar na tela se tomou multa e o nível da dela. 
- velocidade máxima permitida de 80km
- abaixo da velocidade máxima "não houve multa"
- até 10km acima "levou multa leve"
- entre 11 a 20km acima "levou multa grave"
- acima de 20km "levou multa gravíssima"

3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
- O resultado esperado é exibir a mensagem que corresponde ao nível da multa (visando resposta da pergunta 2) que a pessoa levou e exibir também "não houve multa", caso esteja abaixo da velocidade máxima permitida.

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?
input velocidade
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print "Não levou multa"
if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
  print "Levou multa leve"
if velocidade > velocidade_maxima +11 e velocidade <= velocidade_maxima + 20:
  print "Levou multa grave"
if velocidade > velocidade_maxima + 20:
  print "Levou multa gravíssima"
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
  print('Não levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
  print('Levou multa leve')
elif velocidade > velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
  print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
  print('Levou multa gravíssima')
