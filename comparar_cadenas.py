def comparar_cadenas_lexicograficas(cadena1, cadena2):
    #declaración de variables
    valor_cadena1 = 0
    valor_cadena2 = 0

    #recorrer la primera cadena recibida por parametro.
    for char in cadena1:
        #obtener su valor en codigo ASCII
        valor_cadena1 += ord(char)

    # recorrer la primera cadena recibida por parametro.
    for char2 in cadena2:
        # obtener su valor en codigo ASCII
        valor_cadena2 += ord(char2)

    #comparar sus valores..
    if valor_cadena1 < valor_cadena2:
        return -1
    elif valor_cadena2 < valor_cadena1:
        return 1
    else:
        return 0

print(comparar_cadenas_lexicograficas("abc","bcd"))

print(comparar_cadenas_lexicograficas("bcd","abc"))

print(comparar_cadenas_lexicograficas("abc","abc"))