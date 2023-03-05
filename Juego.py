import ModuloJuego

def Juego():
    while True:
        ModuloJuego.Bienvenida()
        ModuloJuego.MenuPrincipal()
        modo = ModuloJuego.Control(1,4)
        if modo != 4:
            ModuloJuego.OpcionesMenu(modo)
        else:
            break


Juego()

