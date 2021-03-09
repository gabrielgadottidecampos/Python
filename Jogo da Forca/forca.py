def jogar():
    print("**********************************")
    print("Bem Vindo ao Jogo da Forcar!")
    print("**********************************")

    palavra_secreta = "banana"
    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip() # tira os espaços da palavra
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): # deixa a palavra digitada e a palavra_secreta em maiusculo, deixando a comparação sempre correta
                print("Encontrei a letra {} na posição {}".format(letra, index))
                index = index + 1
        print("Jogando")


if(__name__ == "__main__"):
    jogar()