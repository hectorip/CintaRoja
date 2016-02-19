# -*- coding: utf-8 -*-

lista = list(range(1, 1000000))
ordenada = []

while lista:
    menor = lista[0]
    for elem in lista[1:]:
        if elem < menor:
            menor = elem
    ordenada.append(menor)
    lista.remove(menor)
    print(lista[0])

print(ordenada)
