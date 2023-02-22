import ModuloJuego
import ModuloEstadistica


def Juego():
    while True:
        ModuloJuego.Bienvenida()
        ModuloJuego.MenuPrincipal()
        modo = ModuloJuego.Control(1,4)
        while modo != 4:
            ModuloJuego.OpcionesMenu(modo)
            break

Juego()


    
    
