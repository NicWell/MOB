#Questão da OBI - Problema do Telefone
#Aluno: Wellington Nicacio


#Entrada

while True:
    entrada = input('Digite os caracteres para conversão:')
    transfList = list(entrada)
    num = []
    #print(len(entrada))
    #print(len(transfList))
    for x in range(len(transfList)):
        #Minúsculo
        if(transfList[x] == 'a' or transfList[x] == 'b' or transfList[x] == 'c'):
            num.append('2')
        if(transfList[x] == 'd' or transfList[x] == 'e' or transfList[x] == 'f'):
            num.append('3')
        if(transfList[x] == 'g' or transfList[x] == 'h' or transfList[x] == 'i'):
            num.append('4')
        if(transfList[x] == 'j' or transfList[x] == 'k' or transfList[x] == 'l'):
            num.append('5')
        if(transfList[x] == 'm' or transfList[x] == 'n' or transfList[x] == 'o'):
            num.append('6')
        if(transfList[x] == 'p' or transfList[x] == 'q' or transfList[x] == 'r' or transfList[x] == 's'):
            num.append('7')
        if(transfList[x] == 't' or transfList[x] == 'u' or transfList[x] == 'v'):
            num.append('8')
        if(transfList[x] == 'w' or transfList[x] == 'x' or transfList[x] == 'y' or transfList[x] == 'z'):
            num.append('9')
        #Maiúsculo
        if(transfList[x] == 'A' or transfList[x] == 'B' or transfList[x] == 'C'):
            num.append('2')
        if(transfList[x] == 'D' or transfList[x] == 'E' or transfList[x] == 'F'):
            num.append('3')
        if(transfList[x] == 'G' or transfList[x] == 'H' or transfList[x] == 'I'):
            num.append('4')
        if(transfList[x] == 'J' or transfList[x] == 'K' or transfList[x] == 'L'):
            num.append('5')
        if(transfList[x] == 'M' or transfList[x] == 'N' or transfList[x] == 'O'):
            num.append('6')
        if(transfList[x] == 'P' or transfList[x] == 'Q' or transfList[x] == 'R' or transfList[x] == 'S'):
            num.append('7')
        if(transfList[x] == 'T' or transfList[x] == 'U' or transfList[x] == 'V'):
            num.append('8')
        if(transfList[x] == 'W' or transfList[x] == 'X' or transfList[x] == 'Y' or transfList[x] == 'Z'):
            num.append('9')
        #Adicionando o hífem
        if(transfList[x] == '-'):
            num.append('-')
    #Saída
    print('='*60)
    numfinal= "".join(num)
    print("Número Correspondente: ",numfinal)
    print("Deseja converter outro número?")
    esc = input("S/N: ")
    print('='*60)
    if(esc == "N" or esc == "n"):
        break
