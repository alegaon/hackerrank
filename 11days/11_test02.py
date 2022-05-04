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
        # retorna la sumatoria del hourglass
        suma = 0
        linea1 = arr[0+y][0+x:3+x]
        for i in linea1:
            suma += i
            
        linea2 = arr[1+y][1+x]
        suma += linea2        

        linea3 = arr[2+y][0+x:3+x]
        for i in linea3:
            suma += i

        return suma

    # como se mueve el reloj de arena?
    # 4 en col y 4 en fila
    # conducta; cada 4 pasos de col(x), baja una fila(y)
    #
    #creo contadores
    avance_col = 0
    avance_row = 0
    while avance_row < 4:

        # tengo que devolver la sumatoria mas alta de los hourglass
        sumatoria_mas_alta = my_hourglass(avance_col, avance_row)
        
        avance_col += 1
        if avance_col == 4:
            avance_col = 0
            avance_row +=1
    

