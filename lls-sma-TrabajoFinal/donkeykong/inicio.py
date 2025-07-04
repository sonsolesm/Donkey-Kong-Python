import pyxel
from .constantes import *

class Inicio:

    #Pintamos los elementos de la pantalla de inicio
    def draw(self):
        pyxel.cls(0)
        pyxel.text(75, 40, "How high can you get?", 7)
        pyxel.blt(95, 100, 1, 5, 58, DK_ANCHO, DK_ALTO)
        pyxel.text(75, 170, "Press enter to start", 7)
        pyxel.text(80, 180, "Press Q to exit", 7)

    #Actualizamos la pantalla de inicio
    def update(self):
        #Si pulsamos Q salimos
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        #Si pulsamos ENTER jugamos
        if pyxel.btn(pyxel.KEY_ENTER):
            return True
        else:
            return False
