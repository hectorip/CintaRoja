'''
Desarrolla un programa que permita leer un valor N
cualquiera y decir si es par o impar.
'''


def even_or_odd():
    n = int(input("Escribe un número por favor: "))
    if n % 2 == 0:
        result = f'{n} es par'
    else:
        result = f'{n} es impar'

    print(result)

even_or_odd()
