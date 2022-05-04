#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

# take my hourglass
# how to do?
# i need a hourglass
# comenzaria de izq a der y de arriba a abajo
# 1er array , tomo los 3 primeros indices
# 2do array, tomo el segundo indice
# 3er array, tomo los 3 primeros indices
# y los sumo y los guardo en un variable
# 
# ahora los mismo pero corriendo 1 indice hacia la derecha
# asi hasta completar la primera linea
# 
#  restricciones
# movimiento del hourglaS de a cuatro pasos por linea y cuatro 
# en columna
#
# tengo q hacer la representacion del hourglass en arrays de 2d

"""
# im making hourglass
# 1ra linea
print(arr[0][0])
print(arr[0][1])
print(arr[0][2])
# 2da linea)
print(arr[1][1])
# 3ra linea)
print(arr[2][0])
print(arr[2][1])
print(arr[2][2])
# bien!!
"""

# ahora a intentar con un for
for row in arr:
    print(row)
    # for col in row:
    #     print(col)

