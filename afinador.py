#-------------------------------------------------------------------------------
# Nombre:        Afinador
# Propósito:Responde a consultas de frecuencias devolviendo descripciones vervales para llegar a notas justas
#
# Author:      Williams cuevas Herrera (@willi_x)
#
# creado:     30/04/2013
# Copyright:   (c) Sensitive Studios 2013
# Licencia:     <gpl>
#-------------------------------------------------------------------------------

#importamos modulos
from notas import afinacion_standard as afst
import pdb

class Afinador(object):
    def __init__(self):
        self.__afinacion=afst.AfinacionStandard()

    def query(self, f):
        #frecuencia delimitadora
        #sirve para saber si hacer el barrido desde arriba o abajo en la  busqueda por la tabla.
        fd=330.0 #frecuencia redondeada
        #obtenemos un switch de inversion para la comparacion de notas
        invertida=False
        #obtenemos tabla de notas
        notas=self.__afinacion.listaNotas
        #obtenemos un rango         de barrido de las 88 teclas del piano, comenzando de 0 a 87
        r=range(0,88)
        #si la frecuencia ingresada es mayor que la frecuencia delimitadora, el rango se invierte para buscar desde arriba
        if f > fd:
            r.reverse()
            invertida=True
        #n representara una nota buscada por la frecuencia dada, con la cual se haran comparaciones
        for i in r:
            n=notas[i]
            if invertida:
                if f >= n.getFreq():
                    break
            else:
                if f <= n.getFreq():
                    break
        c=self.__calculaCents(f,n.getFreq())
        if c>50:
            n=notas[i+1]
            c-=100
        elif c<-50:
            n=notas[i-1]
            c+=100
        if c>0:
            cor="%d cents arriba" %(c)
        elif c<0:
            cor="%d cents abajo" %(c)
        else:
            cor="afinada"
        print "la nota es %s%d, %s." %(n.getNombreAM(), n.getOctava(), cor)

    def __calculaCents(self, f1, f2):
        from math import log
        return int(1200*log(f1/f2,2))
