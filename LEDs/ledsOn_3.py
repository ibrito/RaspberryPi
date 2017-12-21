#!/usr/bin/python
# -*- coding: utf-8 -*-
#+++++++++++++++++++++++++++++
#title           :ledsOn_3.py
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

listaGPIO = [16,17,22]          # aca se cargaran la GPIO que se quieren controlar 


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


#--- Ejecucion

iniGPIO(listaGPIO)              # se configuran todas las salidas definidas en listaGPIO

onTodo(listaGPIO)               # se le envia la orden de poner en 1 todas las salidas de la listaGPIO

time.sleep(2)                   # detiene la ejecución por 2 segundos

L.cleanup()                     # Limpia los canales que se usaron el listaGPIO
