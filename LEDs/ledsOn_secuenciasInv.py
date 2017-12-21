#!/usr/bin/python
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++
#title           :ledsOn_secuenciasInv.py
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
listaGPIO = [16,17,22,23,24,25] # aca se cargaran la GPIO que se quieren controlar
cPines = len(listaGPIO) 
cCiclos   = 0                   # variable para manejar el contador de ciclos de ejecucion
cCiclosMax = 5                  # variable para manejar la cantidad  los ciclos de ejecucion
cT        = 0.3                  # variable para almacenar el tiempo por defecto de 1 segundo


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


def serieUnoLed(lista,cT=0.1): # Enciende un Led a la vez
    
    pX=0
    for pin in lista:
        if (pX == 0):
            L.output(lista[pX],L.HIGH)
            print "0 -I: " + str(pX) + " pin: " + str(pin) + " pinA: " + str(cPines)
            pX +=1
            
        else:
            L.output(lista[pX-1],L.LOW)
            L.output(pin,L.HIGH)
            print "I:" + str(pX) + " pin: " + str(pin) + " pinA: " + str(lista[pX-1])
            pX +=1
        time.sleep(cT)

def serieUnoLedInv(lista,cT=0.1):  # Enciende un Led a la vez Invertido 
    
    pX=0
    for pin in lista:
        if (pX == 0):
            L.output(lista[cPines-(pX+1)],L.HIGH)
            #print "0 -I: " + str(pX) + " pin: " + str(pin) + " pinA: " + str(lista[cPines-1])
            pX +=2
        else:
            #L.output(lista[cPines-(pX-1)],L.LOW)
            L.output(lista[cPines-pX],L.HIGH)
            #print "I:" + str(pX) + " pin: " + str(pin) + " pinA: " + str(lista[cPines-pX])
            pX +=1
        time.sleep(cT)
                


#--- Ejecucion

iniGPIO(listaGPIO)

offTodo(listaGPIO)                               # se configuran todas las salidas definidas en listaGPIO

serieUnoLed(listaGPIO,cT)                       # se invoca la funcion que enciende de forma secuencial

serieUnoLedInv(listaGPIO,cT)                    # se invoca la funcion que enciende de forma secuencial Inv

time.sleep(2)                                   # detiene la ejecución por 2 segundos

L.cleanup()   