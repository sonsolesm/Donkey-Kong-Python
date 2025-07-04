import pyxel

from .personajes.dk import DonkeyKong
from .personajes.mario import Mario
from .personajes.pauline import Pauline

from .escenario.barril import Barriles
from .escenario.escaleras import Escaleras
from .escenario.plataformas import Plataformas
from .escenario.contadores import Contadores

from .inicio import Inicio
from .game_over import GameOver
from .constantes import *

import random

#Clase que controla el juego
class Juego:

    def __init__(self):
        #Iniciamos pyxel, definimos los objetos iniciales del juego, y llamamos a pyxel.run
        pyxel.init(PANTALLA_ANCHO, PANTALLA_ALTO, fps = FPS, caption = "Donkey Kong")

        #Cargamos los bancos de imagenes
        pyxel.image(0).load(0, 0, "assets/imagenes_completas.png")
        pyxel.image(1).load(0, 0, "assets/personajes.png")

        #Creamos la matriz para almacenar las posiciones de las plataformas
        # y las escaleras por las que mario puede moverse
        self.matriz = [[0] * PANTALLA_ALTO for i in range(PANTALLA_ANCHO)]

        #Definimos las escaleras
        self.escaleras = Escaleras()
        #Definimos las plataformas
        self.plataformas = Plataformas()

        #Llamamos a los metodos para anadir las escaleras y plataformas a la matriz
        self.plataformas.definir_matriz(self.matriz)
        self.escaleras.definir_matriz(self.matriz)

        #Metodo para pintar la matriz (comprobacion)
        #self.pintar_matriz()

        #Definimos al jugador mario
        self.mario = Mario(self.matriz)
        #Definimos a Donkey Kong
        self.dk = DonkeyKong()
        #Definimos a Pauline
        self.pauline = Pauline()

        #Definimos los contadores
        self.contadores = Contadores()
        #Creamos la variable puntos
        self.puntos = 0

        #Creamos el contador de los frames
        self.frames = pyxel.frame_count

        #Creamos una lista para los barriles
        self.barriles = []
        self.barriles_maximos = 10

        #Creamos las variables pantalla_inicio y fin_juego
        # para controlar en que pantalla estamos
        self.pantalla_inicio = True
        self.fin_juego= False

        #Creamos la pantalla de inicio y la pantalla fin de juego
        self.Inicio = Inicio()
        self.GameOver = GameOver()


        pyxel.run(self.update, self.draw)

    #Metodo para ver la matriz de movimiento de mario
    def pintar_matriz(self):
        #debug : pintamos la matriz
        import matplotlib.pyplot as plt

        mat = [[self.matriz[j][i] for j in range(len(self.matriz))] for i in range(len(self.matriz[0]))]

        plt.matshow(mat)
        plt.show()


    #Metodo para controlar el choque de mario con barriles
    def choque(self, barril):
        #Comprobamos si la posicion de mario coincide con el margen del barril
        if abs(barril.x - self.mario.x) < 3*BARRIL_ANCHO/4 and abs(barril.y - self.mario.y) < 3*BARRIL_ALTO/4:
            return True
        else:
            return False


    #Metodo para crear los barriles (objetos de la clase barril)
    def lanza_barril(self):
        #Actualizamos a donkey kong para que la animacion coincida con el lanzamiento de los barriles
        self.dk.update()
        if self.dk.estado == 2:
            #Creamos un objeto de la clase barril
            self.barriles.append(Barriles(self.matriz))


    #Metodo para actualizar los puntos de mario
    def subir_puntos(self, barril):
        #Recibe como argumento el barril que hay que comprobar
        #Cuando mario salta un barril suma 100 puntos
        if  abs(self.mario.x - barril.x) < 2\
        and abs(self.mario.y - barril.y) <= 20\
        and not barril.mario_saltado:
            self.puntos += 100
            barril.mario_saltado = True

    #Metodo para actualizar el resto de objetos
    def update(self):
        #Si estamos en la pantalla de inicio esperamos la respuesta del usuario
        if self.pantalla_inicio:
            #Si devuelve true es que quiere jugar y entonces cambiamos de pantalla
            if self.Inicio.update():
                self.pantalla_inicio = False

        #Si estamos en la pantalla fin de juego esperamos la respuesta del usuario
        elif self.fin_juego:
            #Si devuelve true es que quiere jugar y entonces cambiamos de pantalla
            if self.GameOver.update():
                self.mario.x = 20
                self.mario.y = 240
                self.fin_juego = False
                self.pantalla_inicio = True
                self.puntos = 0
                self.mario.vidas = 3
                self.GameOver.ganar = False
                self.barriles = []

        #Si no estamos el pantalla inicio ni en pantalla fin de juego, entonces estamos jugando
        else:
            #Llamamos al metodo ganar para actualizarlo constantemente
            # este metodo compruba si mario gana
            self.ganar()

            #Comprueba si pulsamos Q para salir del juego
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()

            #Llamamos al metodo update de la clase Mario para que se actualizen las variables
            self.mario.update()
            #Llamamos al metodo update de la clase Contadores pasandole las vidas de mario
            self.contadores.update(self.mario.vidas,self.puntos)

            #Checkeamos los frames para lanzar barriles
            if len(self.barriles) < self.barriles_maximos:
                #frame_count controla la velocidad de lanzamiento
                # y las animaciones se coordinan igual
                if pyxel.frame_count - self.frames > FRAMES_BARRILES:
                    self.frames = pyxel.frame_count
                    self.lanza_barril()
                    self.pauline.update()
            else:
                self.dk.estado = 3

            #Creamos una lista para guardar los barriles que hay que quitar
            barriles_quitar = []
            #Creamos la variable muerto para controlar el choque con barriles
            muerto = False

            #Recorremos la lista de barriles y comprobamos para cada uno
            # si se choca contra mario
            for i in range(len(self.barriles)):
                self.barriles[i].update()

                if self.choque(self.barriles[i]):
                    #Si chocamos perdemos una vida y mario vuelve al punto inicial
                    self.mario.vidas -= 1
                    self.mario.x = 20
                    self.mario.y = 240
                    self.mario.saltando = False
                    muerto = True

                    if self.mario.vidas == 0:
                        self.fin_juego = True

                #Si el barril llega al final de la plataforma de abajo y mario no ha muerto
                # entonces se añade a la lista barriles_quitar para ser eliminado
                if self.barriles[i].x == 6 and self.barriles[i].y == 240 and not muerto:
                    barriles_quitar.append(i)

                #Llamamos al metodo para comprobar si mario ha saltado el barril
                self.subir_puntos(self.barriles[i])

            #Si mario muere los barriles se restablecen
            if muerto:
                self.barriles = []
            #Si mario no muere, entonces eliminamos el barril que ha llegado al final
            else:
                for j in barriles_quitar:
                    self.barriles.pop(j)


    #Metodo para comprobar si mario gana llegando hasta Pauline
    def ganar(self):
        if self.mario.x == 128 and self.mario.y == 56:
            self.fin_juego = True
            self.GameOver.ganar = True


    #Metodo para dibujar las imagenes
    def draw(self):
        #Si estamos en la pantalla de inicio la pintamos
        if self.pantalla_inicio:
            self.Inicio.draw()

        #Si estamos en la pantalla fin de juego la pintamos
        elif self.fin_juego:
            self.GameOver.draw()

        #Si no estamos en la pantalla de inicio ni en la de fin de juego
        # entonces estamos jugando y pintamios la pantalla del juego
        else:
            #Ponemos el fondo en color negro y borramos cualquier otra cosa que haya en la pantalla
            pyxel.cls(0)

            #Pintamos las escaleras
            self.escaleras.draw()
            #Pintamos las plataformas
            self.plataformas.draw()

            #Llamamos al metodo draw de la clase DonkeyKong para que se pinte
            self.dk.draw()
            #Llamamos al metodo draw de la clase Mario para que se pinte
            self.mario.draw()
            #Llamamos al metodo draw de la clase Pauline para que se pinte
            self.pauline.draw()

            #Llamamos al metodo draw de la clase Contadores
            self.contadores.draw()

            #Llamamos al metodo draw de la clase Barril para cada uno de los barriles para que se pinten
            for barril in self.barriles:
                barril.draw()
