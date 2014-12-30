from nota import Nota
class AfinacionStandard(object):
    def __init__(self, referencia=440.0):
        self.r12=2**(1.0/12.0)
        self.__nombreNotas=['do',
        'do sostenido',
        'Re',
        'Re sostenido',
        'Mi',
        'Fa',
        'Fa sostenido',
        'Sol',
        'Sol sostenido',
        'La',
        'La sostenido',
        'Si']
        self.__nombreNotasAM=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.referencia=referencia
        self.listaNotas=[]
        octava=0
        inota=10
        i=1
        while i<=88:
            if inota>12:
                inota=1
                octava+=1
            #ahora obtenemos algunos parametros de la lista de notas
            nn=self.__nombreNotas[inota-1] #para hacerlo concordar con los indices partidos en 0 de python
            nna=self.__nombreNotasAM[inota-1]
            freq=self.__frecuenciaNota(octava, inota)
            #creamos una nota temporal
            notatemp=Nota(i, octava, nn, nna, freq)
            #la agregamos a la lista de notas
            self.listaNotas.append(notatemp)
            inota+=1
            i+=1

    def __frecuenciaNota(self, octava, nota):
        referencia=self.referencia #referencia de 440HZ
        r12=self.r12 #raiz duodecima de 2
        return round(referencia*r12**((octava-4)*12+(nota-10)),6)
