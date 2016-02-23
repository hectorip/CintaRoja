'''
El emperador Julio César protegía su unformación con
encriptación rotando N veces las letras de un String.
Desarrolla un programa que encripte un mensaje dado el
mensaje y un número N que indique la rotación de las letras.
Los símbolos no se rotan.
'''


def encrypt(message, n):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'
                'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_length = len(alphabet)
    encrypted_message = ""
    for c in message.lower():
        new_index = alphabet[c] + n
        if new_index >= alphabet_length:
            new_index = new_index - alphabet_length

        encrypted_message += alphabet_length[new_index]

    print(encrypted_message)

encrypt("Hola")
