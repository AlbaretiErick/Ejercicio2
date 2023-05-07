class ViajeroFrecuente:
    __num_viajero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0
    def __init__(self, num_viajero, nombre, apellido, dni, millas_acum):
        self.__num_viajero = num_viajero
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__millas_acum = int(millas_acum)
    def cantidadTotalMillas (self):
        return self.__millas_acum
    def acumularMillas (self, cantMillas):
        self.__millas_acum = int(self.__millas_acum) + int(cantMillas)
        return self.__millas_acum
    def canjearMillas (self, millasXcanjear):
        if int (millasXcanjear) <= self.__millas_acum:
            m = int(self.__millas_acum) - int(millasXcanjear)
        else:
            print ('Error en la operacion: Cantidad de millas insuficiente.')
            m = -1
        return m
    def buscar (self, num):
        marca = False
        if num == self.__num_viajero:
            marca = True
        return marca