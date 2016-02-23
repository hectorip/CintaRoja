import math
'''
Desarrolla un programa que calculea cuántos CDs se necesitan
para respaldar la información de un disco duro de capacidad desconocida
(input) considerando que la capacidad del disco está expresada en GB y la
del CD es de 700MB.
'''


def how_many_cds(hd_size, cd_capacity=700):
    rough_capacity = (hd_size * 1024) / cd_capacity
    return math.ceil(rough_capacity)
