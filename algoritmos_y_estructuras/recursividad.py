# Punto de Terminción

# [1 , 2 , 3 ,4, 6]

# elem_0 + suma del resto
            # primer 

# suma de una lista de un elmento es el elemento mismo


def suma(lista):
    if lista:
        return lista[0] + suma(lista[1:])
    else:
        return 0

print(suma([1, 2, 3, 4]))
