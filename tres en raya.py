class CeldaOcupada:
    def __init__(self):
        Exception.__init__(self,"La celda esta ocupada")

class Jugador:
    def __init__(self,nombre,tipoficha):
        self.__nombre=nombre
        self.__tipoficha=tipoficha
        self.__puntuacion=0

    def __str__(self):
        return (self.__nombre + " " +self.__tipoficha + " " +self.__puntuacion)

    def get_nombre(self):
        return self.__nombre
    def get_tipo_ficha(self):
        return self.__tipoficha
    def get_puntuacion(self):
        return self.__puntuacion
    def actualizacion(self):
        self.__puntuacion=self.__puntuacion+1
class Celda:
    def __init__(self,i,j):
        self.__columna=j
        self.__fila=i
        self.__esta_vacia= True

    def __str__(self):
        if(self.__esta_vacia):
            return (" ")
        else:
            return (self.__ficha)

    def asignar_ficha(self,ficha):
        if(self.__esta_vacia):
            self.__ficha=ficha
            self.__esta_vacia=False
        else:
            raise CeldaOcupada
    def reiniciar_ficha(self):
        self.__esta_vacia=True
        self.__ficha=None
class Tablero:
    def __init__(self):
        self.__alto=3
        self.__ancho=3
        self.__matriz_celdas =[]
        linea=[]
        for j in range(self.__alto):
            for i in range(self.__ancho):
                linea.append(Celda(i,j))
            self.__matriz_celdas.append(linea)
        self.__numero_fichas=0
def poner_ficha(self,i,j,ficha):
    #try:
        self.__matriz_celdas[i][j].asignar_ficha(ficha)
   # except CeldaOcupada:
def reiniciar_tablero(self):
    self.__numero_fichas=0
    for i in range(self.__alto):
        for j in range(self.__ancho):
            self.__matriz_celdas[i][j].reiniciar_ficha()
def hay_tres_raya(self):