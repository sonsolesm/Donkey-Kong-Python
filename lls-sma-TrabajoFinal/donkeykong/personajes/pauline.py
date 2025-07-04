import pyxel

class Pauline:

    def __init__(self):
        #Creamos las variables para cada objeto de la clase
        self.__estado = 0

    #Metodo para actualizar el estado de Pauline
    def update(self):
        self.__estado += 1
        #Con el modulo cuando el estado llega hasta 2 vuelve a ser 0
        self.__estado = self.__estado % 2

    #Metodo para pintar a Pauline
    def draw(self):
        if self.__estado == 0:
            #Pauline parada
            pyxel.blt(90, 56-22, 1, 54, 179, 16,22)
        if self.__estado == 1:
            #Pauline pidiendo ayuda
            pyxel.blt(90, 56-22, 1, 31, 179, 16,22)
            pyxel.blt(110, 56-22, 1, 126, 182, 23,8)
