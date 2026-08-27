entrada = input("Entrada: ")
i = 0

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
        while i < len(entrada):
            if entrada[i] == '=':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '=':
                        token += entrada[i]
                        i += 1
                            
                print(token, " -> Caracter especial")
                        

            elif entrada[i] == '<':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '=':
                        token += entrada[i]
                        i += 1

                print(token, " -> Caracter especial")
                        

            elif entrada[i] == '>':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '=':
                        token += entrada[i]
                        i += 1

                print(token, " -> Caracter especial")
                        

            elif entrada[i] == '!':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '=':
                        token += entrada[i]
                        i += 1

                print(token, " -> Caracter especial")
                        

            elif entrada[i] == '&':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '&':
                        token += entrada[i]
                        i += 1

                print(token, " -> Caracter especial")
                        

            elif entrada[i] == '|':
                token = entrada[i]
                i += 1
                while i < len(entrada):
                    if entrada[i] == '|':
                        token += entrada[i]
                        i += 1

                print(token, " -> Caracter especial")
                        
                    

            else:
                token = entrada[i]
                print(token, " -> Caracter especial")
                i += 1