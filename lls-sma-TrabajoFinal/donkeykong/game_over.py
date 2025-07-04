import pyxel
from .constantes import *

class GameOver:
    def __init__(self):
        self.ganar = False

    #Pintamos los elementos de la pantalla de fin de juego
    def draw(self):
        #Si perdemos mostramos GAME OVER
        if not self.ganar:
            pyxel.cls(0)
            pyxel.text(95, 100, "GAME OVER", 8)
            pyxel.text(65, 120, "Press enter to play again", 7)
            pyxel.text(80, 140, "Press Q to exit", 7)
        #Si ganamos mostramos YOU WON
        else:
            pyxel.cls(0)
            pyxel.text(95, 100, "YOU WON!!!", 12)
            pyxel.text(65, 120, "Press enter to play again", 7)
            pyxel.text(80, 140, "Press Q to exit", 7)
    #Actualizamos la pantalla de fin de juego
    def update(self):
        #Si pulsamos ENTER volvemos a jugar
        if pyxel.btn(pyxel.KEY_ENTER):
            return True
        #Si pulsamos Q salimos
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()
