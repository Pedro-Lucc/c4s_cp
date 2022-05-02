#DEFININDO UM NÚMERO SECRETO
#numeroAleatorio = int(input("NÚMERO SECRETO É: "))

numeroAleatorio = int(6)
nRand = int(4)
clue = ""
msg = ""
tentativa = int(1)
maxTentativas = int(3)
t = ""
restante = int(-1)


while tentativa <= maxTentativas:
    restante = maxTentativas - tentativa
    if tentativa < maxTentativas:
      t = ("RESTAM " , restante , " TENTATIVAS!!!!!")
    if nRand == numeroAleatorio:
        msg = "Parabéns você acertou o número secreto que é: " , nRand
    else:
        msg = "ERRO – Tente novamente, o numero secreto não é: " , numeroAleatorio

        if numeroAleatorio < nRand:
            clue = "O NÚMERO INSERIDO É MENOR QUE O NÚMERO ALEATÓRIO"
        else:
            clue = "O NÚMERO INSERIDO É MAIOR QUE O NÚMERO ALEATÓRIO"
        print(msg)
        print(clue)
    tentativa = tentativa + 1








