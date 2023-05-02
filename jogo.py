import random
import time

tentativas = -1
acertou = False
print("Bem vindo ao jogo de adivinhação!")
nome_usuario = input('Qual o seu nome? ')

while True:
  print("Bem vindo ao jogo de adivinhação!")
  numero_secreto = random.randint(1, 100)
  i = 0
  print("Menu de Opções: \n")
  print("F - Fácil\n")
  print("M - Médio\n")
  print("D - Difícil\n")
  nivel = input('Qual o nivel do jogo?')
  nivel_do_jogo = str(nivel)

  if nivel_do_jogo == "F":
    tentativas = 10
  if nivel_do_jogo == "M":
    tentativas = 5
  if nivel_do_jogo == "D":
    tentativas = 3

  tempo_incial = int(time.time())
  while i < tentativas:
    palpite = int(input("Qual o seu palpite? "))

    print(f'O usuario {nome_usuario} deu o palpite {palpite}')
    i += 1
    if (palpite == numero_secreto):
      tempo_final = int(time.time())
      print(f'{nome_usuario} voce acertou o numero {numero_secreto}\n')
      acertou = True
      print(f'O número de palpites dados foi {i}')
      print(
        f'O tempo de execução foi de {tempo_final - tempo_incial} segundos')
      resposta = input('Deseja jogar novamente? s-sim n-não')
      if (resposta == 's'):
        i = 0
        break
      else:
        break
    else:
      print(f'{nome_usuario} voce errou o numero secreto!')
      if (i == tentativas):
        break
      if (palpite < numero_secreto):
        print(f'{nome_usuario} voce errou para baixo! Informe um numero maior')
      else:
        print(f'{nome_usuario} voce errou para cima! Informe um numero menor')

  if (acertou == False and i == tentativas):
    print(f"Você errou! O número secreto era {numero_secreto}")
    resposta_dois = input('Deseja jogar novamente? s-sim n-não')
    if (resposta_dois == 's'):
      i = 0
      continue
    else:
      break

  if (resposta == 'n'):
    break
