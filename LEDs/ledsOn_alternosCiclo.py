#!/usr/bin/python
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++
#title           :ledsOn_alternosCiclo.py
#description     :Script en python para encender 3 LEDs
#author          :Irving Brito
#date            :21-12-2017
#Placa           :Raspberry Pi B+ V1.2
#lenguaje        :Python
#++++++++++++++++++++++++++++++
import RPi.GPIO as L  
import time
L.setmode(L.BCM)                # inicializar la placa en modo BCM
L.setwarnings(False)            # se apagan las advertencias
listaGPIO = [16,17]          	# aca se cargaran la GPIO que se quieren controlar 
cCiclos	  = 0               # variable para manejar el contador de ciclos de ejecucion
cCiclosMax = 5				# variable para manejar la cantidad  los ciclos de ejecucion
cT	      = 1 				 	# variable para almacenar el tiempo por defecto de 1 segundo


#--- Definicion de funciones
def iniGPIO(lista):             # funcion para inicializar las GPIO como salidad listadas en listaGPIO
    for pin in lista:
        L.setup(pin,L.OUT)

def offTodo(lista):             # funcion para apagar o poner en 0 todas las GPIO de la listaGPIO
    for pin in lista:
        L.output(pin,L.LOW)

def onTodo(lista):              # funcion para encender o poner en 1 todas las GPIO de la listaGPIO
    for pin in lista:
        L.output(pin,L.HIGH)


def ciclosAlternos(lista, cCiclos,cCiclosMax):       # Funcions para encender de forma alterna dos leds con un ciclo
    while cCiclos < cCiclosMax:
        L.output(lista[0],L.HIGH)
        L.output(lista[1],L.LOW)
        time.sleep(cT)
        L.output(lista[0],L.LOW)
        L.output(lista[1],L.HIGH)
        time.sleep(cT)
        cCiclos += 1
        print "Ciclos Totales:" + str(cCiclosMax) + " ciclo Actual: " + str(cCiclos)        


#--- Ejecucion

iniGPIO(listaGPIO)                              # se configuran todas las salidas definidas en listaGPIO

ciclosAlternos(listaGPIO,cCiclos,cCiclosMax)    # se invoca la funcion que enciende de forma alterna los leds

time.sleep(2)                                   # detiene la ejecución por 2 segundos

L.cleanup()   