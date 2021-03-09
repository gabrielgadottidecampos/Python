import random
print("**********************************")
print("Bem Vindo ao Jogo de Adivinhação!")
print("**********************************")

numero_secreto = random.randrange(1,101)
total_tentativas = 0
pontos = 1000

print("Qual o nivel de dificuldade? ")
print("[1] Facil [2] medio [3] dificil")
nivel = int(input("Digite a dificuldade"))
if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

rodada = 1
# while (rodada <= total_tentativas):
for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))  # interpolação de string
    chute_str = input("Digite o seu número ente 1 e 100: ")
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!!! e fez {} pontos".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! o seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! o seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

print("Fim de Jogo")
