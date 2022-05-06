# buscando variables

def total(resultado_del_porcentaje, porcentaje):
    return (resultado_del_porcentaje * 100) / porcentaje  

def resultado_del_porcentaje(total, porcentaje):
    return (total * 100 ) / porcentaje

def porcentaje(resultado_del_porcentaje, total):
    return  resultado_del_porcentaje / (total * 100)

# otras funciones para hacer los input de numeros

def ingresar_numero(dato):
    while True:
        try:
            numero = int(input(f"Escribi tu {dato} buscado: "))
            break
        except ValueError:
            print("DALE PAH!.. q paso? Solo escribi numeros")
            print("ej: 1 , 2 , 454654... okas??")
            print("vamo' de nuevo")
    return numero

# voy por el lado de una app
# menu
while True:
    print("/////////////////////////////")
    print("")
    print("eleji la variable a despejar:")
    print("""
    1 - total
    2 - resultado del porcentaje
    3 - porcentaje %
    4 - terminar
    """)

    opcion = input("escriba el N° de opcion: ")
    print("")
    print("/////////////////////////////")

    # 4 para salir
    if opcion == "4":
        break

    # 1 despeja tota
    if opcion == "1":
        print("total")
        tu_resultado_porcentaje = ingresar_numero("resultado del porcentaje")
        tu_porcentaje = ingresar_numero("porcentaje")
        tu_total = total(tu_resultado_porcentaje, tu_porcentaje)
        print(f"tu total es: {tu_total}")
        