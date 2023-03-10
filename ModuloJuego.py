import random
import getpass

import ModuloEstadistica


def Bienvenida():
    print("\n¡Bienvenido al Juego de las Adivinanzas!\n")
    input("Pulse ENTER para iniciar")
    

def MenuPrincipal():
    print("\nMenu")
    print("1. Partida modo solitario")
    print("2. Partida 2 jugadores")
    print("3. Estadística")
    print("4. Salir")


def Control(min,max):
    opcion = 0   
    while opcion < min or opcion > max:
        opcion = int(input("\nElija una opción del menu: "))
    else:
        return opcion
            

def MenuDificultad():
    print("\nDificultad")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")
    print("4. Dificultad según número a adivinar")


def OpcionesMenu(opcion):
    if opcion == 1 or opcion == 2:
        MenuDificultad()
        dificultad = Control(1,4)
        Dificultad(dificultad,opcion)
    elif opcion == 3:
        MenuEstadistica()
        estadistica = Control(1,2)
        Estadistica(estadistica)


def Dificultad(dificultad, modo):
    if dificultad == 1:
        numero = Numero(modo)
        print("\nTiene 20 intentos para adivinar el número entre 1 y 1000")
        Adivina(numero,21)
    elif dificultad == 2:
        numero = Numero(modo)
        print("\nTiene 12 intentos para adivinar el número entre 1 y 1000")
        Adivina(numero,13)    
    elif dificultad == 3:
        numero = Numero(modo)
        print("\nTiene 5 intentos para adivinar el número entre 1 y 1000")
        Adivina(numero,6)
    else: 
        numero = Numero(modo)
        intentos_totales = DificultadMisterio(numero)
        Adivina(numero,intentos_totales)
        

def Numero(modo):
    if modo == 1:
        numero = random.randint(1,1001)
    elif modo == 2:
        numero = int(getpass.getpass("\nJugador 1 introduzca un número del 1 al 1000: "))
        while numero < 1 or numero > 1000:
            numero = int(getpass.getpass("\nJugador 1 introduzca un número del 1 al 1000: "))
    return numero


def Adivina(numero,intentos_totales):            
    i = intentos_totales - 1

    while i in range(1,intentos_totales):
        jugador = int(input("\nAdivine el numero entre 1 y 1000: "))

        i = i - 1

        if jugador > numero:
            print("El número buscado es menor.")
        elif jugador < numero:
            print("El número buscado es mayor.")
        elif jugador == numero:
            print("\n¡Ha ganado el juego en " + str(intentos_totales-i-1) + " intentos!")
            break 
                
        if i == 0:
            print("\nHa perdido el juego")
            break 
                
    ModuloEstadistica.Resultados(i, intentos_totales)


def DificultadMisterio(numero):
    if numero <= 200:
        intentos_totales = 5
    elif numero > 200 and numero <= 600:
        intentos_totales = 12
    elif numero > 600 and numero <= 1000:
        intentos_totales = 20

    print("\nTiene " + str(intentos_totales) + " intentos para adivinar el número entre 1 y 1000")

    return intentos_totales


def MenuEstadistica():
    print("\nEstadísticas")
    print("1. Cantidad de partidas ganadas y perdidas")
    print("2. Intentos utilizados")


def Estadistica(estadistica):
    if estadistica == 1:
        ModuloEstadistica.GanadosPerdidos()
    else:
        ModuloEstadistica.Intentos()