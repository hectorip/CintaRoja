'''
Un programa que reciba un número indeterminado de
letras (mayúsculas o minúsculas) e indique cuántas
vocales y cuántas consonantes entraron.
'''


def vowels_and_consonants(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_count = 0
    consonant_count = 0
    for l in letters:
        if l.lower() in vowels:
            vowels_count += 1
        else:
            consonant_count += 1

    print("Input: " + str(letters))
    print("Número de vocales: " + str(vowels_count) +
          "\nNúmero de consonantes:" + str(consonant_count))


vowels_and_consonants("aeiouaeioulll")
