'''
Un programa que  solicite 2 valores numéricos y después
un operador aritmético (*,+,/,-) y devuelva el resultado de la operación
'''


def calc():
    n_1 = int(input("Primer valor: "))
    n_2 = int(input("Segundo valor: "))
    operator = input("Escribe el operador: ")

    if operator == "+":
        print(n_1 + n_2)
    elif operator == "-":
        print(n_1 - n_2)
    elif operator == "*":
        print(n_1 * n_2)
    elif operator == "/":
        print(n_1/n_2)


def calc_lambda():
    n_1 = int(input("Primer valor: "))
    n_2 = int(input("Segundo valor: "))
    operator = input("Escribe el operador: ")

    operations = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y,
        "/": lambda x, y: x/y,
    }
    selected_operation = operations[operator]
    print(selected_operation(n_1, n_2))

calc_lambda()
