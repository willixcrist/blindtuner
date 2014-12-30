# Nombre:        module1
# Prop?sito:
#Manejar el stream de audio para el afinador.
# Author:      Estefi
#
# creado:     30/01/2012
# Copyright:   (c) Estefi 2012
# Licencia:     GPL
#-------------------------------------------------------------------------------
class AudioStream(object):
    def __init__(self):
        import pyaudio
        #declaraci?n de los formatos predeterminados
        self.format=pyaudio.paInt16
        self.samplerate=44100
        self.short_normalize=(1.0/32768.0)
        self.channels=2
self.input_block_time=0.05
