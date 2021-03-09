numero_magico = 30
tentativas = 3
rodada = 1
for rodada in range(1, tentativas + 1):
    chute_str = input("Digite um número entre 1 e 100: ")
    chute = int(chute_str)
    if (chute < 1 or chute > 100):
        print("número invalido! digite um número entre 1 e 100")
        continue
    else:
        acertou = chute == numero_magico
        maior = chute > numero_magico
        menor = chute < numero_magico
        if(acertou):
            print("Parabéns você acertou! número digitado {} número magico {}".format(chute, numero_magico))
            break
        if(maior):
            print("Você digitou um número maior que o número magico")
        else:
            print("Você digitou um número menor do que o número magico")
