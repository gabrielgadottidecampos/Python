def jogar():
    print("**********************************")
    print("Bem Vindo ao Jogo da Forcar!")
    print("**********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    enforcou = False
    acertou = False
    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite uma letra: ")
        chute = chute.strip() # tira os espaços da palavra
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): # deixa a palavra digitada e a palavra_secreta em maiusculo, deixando a comparação sempre correta
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)


if(__name__ == "__main__"):
    jogar()

#################################################
"""
strip() -> tira os espaço da palavra 
upper() -> trasforma todas as letras em maiuscula 
capitalize() -> Palavra inicia em maiusculo  

"""
