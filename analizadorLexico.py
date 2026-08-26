entrada = input("Entrada: ")
i = 0

def comparar (comparar):
    caracteres = ["+", "-", "*","/","<", ">", "=", "|", "&", "!", ";", ",", "(", ")", "{", "}", "$"]
    x = 0
    while x < len(caracteres):
        if comparar == caracteres[x]:
            return caracteres[x]
        else:
            x +=1

while i < len(entrada):

    #Identificador de espacios
    if entrada[i] == ' ':
        i += 1
        continue
    #Identificador de palabras reservadas e identificadores
    if entrada[i].isalpha():
        token = ""

        while i < len(entrada) and entrada[i].isalpha():
            token += entrada[i]
            i += 1

        print(token, "-> IDENTIFICADOR")
    #Identificador de enteros
    elif entrada[i].isdigit():
        token = ""

        while i < len(entrada) and entrada[i].isdigit():
            token += entrada[i]
            i += 1
        #Identificador de Reales
        if i < len(entrada) and entrada[i] == '.':
            token += '.'
            i += 1 

            while i < len(entrada) and entrada[i].isdigit():
                token += entrada[i]
                i += 1

            print(token, "-> REAL")

        else:
            print(token, "-> ENTERO")
    #Identificador de caracteres especiales 
    else:
        token = comparar(entrada[i])
        i +=1 
        contador = 0
        while contador < 2:
            if token == comparar(entrada[i]):
                token += entrada[i]
                i += 1
                contador += 1
            else:
                token += comparar(entrada[i])
                i += 1
                contador += 1
                break
        print(token, " -> Caracter especial")

    