#-------------------------------------------------------------------------------
# Nombre:        module1
# Propósito:
#Representa una nota en el afinador
# Author:      Estefi
#
# creado:     30/01/2012
# Copyright:   (c) Estefi 2012
# Licencia:     <your licence>
#-------------------------------------------------------------------------------
class Nota(object):
    def __init__(self, index, octave, name, american_name, freq):
        self.__octave=octave
        self.__name=name
        self.__american_name=american_name
        self.__freq=freq
        self.__index=index

    def getNombre(self):
        return self.__name

    def getNombreAM(self):
        return self.__american_name

    def getOctava(self):
        return self.__octave

    def getFreq(self):
        return self.__freq

    def indice():
        return self.__index
