entrada = input("Entrada: ")
i = 0

while i < len(entrada):

    if entrada[i] == ' ':
        i += 1
        continue

    if entrada[i].isalpha():
        token = ""

        while i < len(entrada) and entrada[i].isalpha():
            token += entrada[i]
            i += 1

        print(token, "-> IDENTIFICADOR")

    elif entrada[i].isdigit():
        token = ""

        while i < len(entrada) and entrada[i].isdigit():
            token += entrada[i]
            i += 1

        if i < len(entrada) and entrada[i] == '.':
            token += '.'
            i += 1 

            while i < len(entrada) and entrada[i].isdigit():
                token += entrada[i]
                i += 1

            print(token, "-> REAL")

        else:
            print(token, "-> ENTERO")

    else:
        print(entrada[i], "-> ERROR")
        i += 1