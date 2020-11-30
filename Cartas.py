while True:
    a = int(input("Digite o Nº da carta: "))
    b = int(input("Digite o Nº da carta: "))
    c = int(input("Digite o Nº da carta: "))

    if a == b:
        print(c)
        break
    elif a==c:
        print(b)
        break
    elif b == c:
        print(a)
        break
    else:
        print("Não encontramos pares entres os números fornecidos!")
        print("TENTE NOVAMENTE:")