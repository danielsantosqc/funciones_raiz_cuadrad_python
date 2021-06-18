from datetime import datetime
import time

def enumeracion_exaustiva(objetivo):
    respuesta = 0
    while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene una raiz cuadrada exacta')


def aproximacion_soluciones(objetivo):
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo)>= epsilon:
        print(f'No se encontro la raiz cuadrada del objetivo {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    now = datetime.now()
    end_time = now.strftime("%H:%M:%S")
    print("start_time =", start_time)
    print("End Time =", end_time)


def busqueda_binaria(objetivo):
    epsilon = 0.01
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto+bajo)/2
    now = datetime.now()
    start_time = now.strftime("%H:%M:%S")
    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        
        respuesta = (alto + bajo)/2
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
    now = datetime.now()
    end_time = now.strftime("%H:%M:%S")
    print("start_time =", start_time)
    print("End Time =", end_time)

def funcion_selector():
    selector = int(input("""Elije un numero para la opcion, con la cual 
    quieres hallar la raiz cuadrada
    1.-Enumeracion Exaustiva.
    2.-Aproximacion de Soluciones
    3.-Busqueda Binaria
    """))
    if selector == 1 or selector == 2 or selector == 3:
        print (f'selector+++{selector}')#aqui comprovamos el valor a retornar
        return selector
    else:
        print("No elegiste una de las opciones disponibles")
        time.sleep(1)
        # del selector
        funcion_selector()
            

def run():
    selector = funcion_selector()
    print(f'slector----{selector}')# aqui verificamos el valor recibido de funcion_selector 
    objetivo = int(input("Muy bien. Ahora dime un numero:  "))
    if selector == 1:
        enumeracion_exaustiva(objetivo)
    elif selector == 2:
        aproximacion_soluciones(objetivo)
    elif selector == 3:
        busqueda_binaria(objetivo)
    else:
        print('algo esta mal')

if __name__ == '__main__':
    run()