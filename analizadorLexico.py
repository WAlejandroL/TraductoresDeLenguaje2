entrada = input("Entrada: ")
i = 0

def validar(valor):
    tipo = 0
    i = 0
    diccionario = [["id", 0],
                   ["entero", 1],
                   ["real", 2],
                   ["cadena", 3],
                   ["int", 4], 
                   ["float", 4], 
                   ["void", 4], 
                   ["+", 5], 
                   ["-", 5], 
                   ["*", 6], 
                   ["/", 6], 
                   ["<", 7], 
                   [">", 7], 
                   ["<=", 7],
                   [">=", 7],
                   ["||", 8],
                   ["&&", 9],
                   ["!", 10],
                   ["==", 11],
                   ["!=", 11],
                   [";", 12],
                   [",", 13],
                   ["(", 14],
                   [")", 15],
                   ["{", 16],
                   ["}", 17],
                   ["=", 18],
                   ["if", 19],
                   ["while", 20],
                   ["return", 21],
                   ["else", 22],
                   ["$", 23]]

    bandera = 0
    for i in range(len(diccionario)):
        if valor == diccionario[i][0]:
            tipo = diccionario[i][1]
            bandera = 1
            break

    if bandera == 0: 
        if valor[0].isalpha():
            tipo = diccionario[0][1]

        else:
            tipo = -1
            print("Error léxico: ", valor)

    return tipo

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

        print(token, "->", validar(token))

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
            val = "real"
            print(token, "->", validar(val))

        else:
            val = "entero"
            print(token, "->", validar(val))

    #Identificador de caracteres especiales 
    else:
        if entrada[i] == '=':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '=':
                token += entrada[i]
                i += 1
                        
            print(token, " ->", validar(token))                  

        elif entrada[i] == '<':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '=':
                token += entrada[i]
                i += 1

            print(token, " ->", validar(token))                   

        elif entrada[i] == '>':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '=':
                token += entrada[i]
                i += 1

            print(token, " ->", validar(token))           

        elif entrada[i] == '!':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '=':
                token += entrada[i]
                i += 1

            print(token, " ->", validar(token))      

        elif entrada[i] == '&':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '&':
                token += entrada[i]
                i += 1

            print(token, " ->", validar(token))
                    

        elif entrada[i] == '|':
            token = entrada[i]
            i += 1

            if i < len(entrada) and entrada[i] == '|':
                token += entrada[i]
                i += 1

            print(token, " ->", validar(token))
                    
        else:
            token = entrada[i]
            print(token, " ->", validar(token))
            i += 1