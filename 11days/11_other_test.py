# row_Size = 2
# col_Size = 4
# my_array = row_Size
# 
# print(my_array  )


# comprehension list
# lista dicc tuplas
import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # i have to for to append hourglass

    def my_hourglass(x,y):
        # tengo mi hourglass 
        # "x" e "y" sirve para moverlo segun sus ejes
        suma = 0
        linea1 = arr[0+y][0+x:3+x]
        print(f'linea 1: x:{x},y{y}<{arr[0+y][0+x:3+x]}>')
        for i in linea1:
            suma += i
            
        linea2 = arr[1+y][1+x]
        print(f'linea 2: x{x},y:{y}<    {arr[1+y][1+x]}   >')
        suma += linea2        

        linea3 = arr[2+y][0+x:3+x]
        print(f'linea 3: x{x},y:{y}<{arr[2+y][0+x:3+x]}>')
        for i in linea3:
            suma += i

        return f'suma del hourglass{suma}'

    # como se mueve el reloj de arena?
    # 4 en col y 4 en fila
    # conducta; cada 4 pasos de col(x), baja una fila(y)
    #
    #creo contadores
    avance_col = 0
    avance_row = 0
    while avance_row < 4:
        print(my_hourglass(avance_col, avance_row))
        avance_col += 1
        if avance_col == 4:
            avance_col = 0
            avance_row +=1
            print(f"fila {avance_row}")
    

#    print(my_hourglass(2,2))
# im making hourglass
# 1ra linea
# [0][0]
# [0][1]
# [0][2]
# # 2da linea
# [1][1]
# # 3ra linea
# [2][0]
# [2][1]
# [2][2]

# con un for
