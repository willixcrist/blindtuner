#-------------------------------------------------------------------------------
# Nombre:        module1
# Propósito:
#
# Author:      Estefi
#
# creado:     03/02/2012
# Copyright:   (c) Estefi 2012
# Licencia:     <your licence>
#-------------------------------------------------------------------------------
"""Representa un block de audio con propiedaes que facilitan el cálculo de frecuencia"""
from struct import unpack
class AudioBlock(object):
    def __init__(self, wav_block, data_size, frame_rate):
        self.__data=wav_block
        self.__data_size=data_size
        self.__frame_rate=frame_rate

    def get_data(self):
        """Devuelve los datos ya unpacados para el manejo numérico en un array."""
        data=unpack("[n]h".format(n=self.__data_size), self.__data)
        return data

    def rms_amplitude(self):
