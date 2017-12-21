# LEDs
Scripts para control de LEDs con Raspberry Pi B+ y Python

## Montaje
Los scripts usados para las pruebas usan como configuracion de la Raspberry Pi B+  el sigiente espema, tambien dejo la configuracion en la protoboard,
el Sistema Operativo ([Raspbian](https://www.raspberrypi.org/downloads/raspbian/)) :

*	Raspbian Stretch with desktop
*	Image with desktop based on Debian Stretch
*	Version: November 2017
*	Release date: 2017-11-29
*	Kernel version: 4.9

### Esquema 
 ![Esquema Raspberry Pi B+ ](https://github.com/ibrito/RaspberryPi/blob/master/LEDs/rpi_B_LEDs_esquema.png "Esquema rspberry Pi b+ ")

### Protoboard
![Protoboard Raspberry Pi B+ ](https://github.com/ibrito/RaspberryPi/blob/master/LEDs/rpi_B_LEDs_protoboard.png "Protoboard rspberry Pi b+ ")

## ledsOn_1.py
#### Uso

La ejecución de este script encendera el LED numero 1  conectado a la GPIO 16 de la raspberry Pi B+

```py
 sudo python ledsOn_1.py

```

En el script podremos ver tres partes, donde están la importaciones de las librerias RPi.GPIO y time conjuntamente con la definicón de varibles, la segunda donde se encuentra definidas las funciones y la ultima donde se llaman estas funciones y se ejecuta el encendido del LED

#### Parte 1:

```py
import RPi.GPIO as L  
import time
L.setmode(L.BCM)                # inicializar la placa en modo BCM
L.setwarnings(False)            # se apagan las advertencias

listaGPIO = [16]                # aca se cargaran la GPIO que se quieren controlar 

```
Por ejemplo si queremos agregar mas de una salida solo deberemos agregar el numero de GPIO que queremos usar a la lista (listaGPIO[])
```py
listaGPIO = [16,17]	#aca se agrego el GPIO 17 a la lista, ahora se ejecutaran las funciones para estad dos GPIO

```


#### Parte 2:
```py

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

```

#### Parte 3:
```py

#--- Ejecucion

iniGPIO(listaGPIO)              # se configuran todas las salidas definidas en listaGPIO

onTodo(listaGPIO)               # se le envia la orden de poner en 1 todas las salidas de la listaGPIO

time.sleep(2)                   # detiene la ejecución por 2 segundos

L.cleanup()                     # Limpia los canales que se usaron el listaGPIO

```
_________________________________________________________________________

## ledsOn_3.py
#### Uso
La ejecución de este script encendera el LED numero 1,2,3  conectado a la GPIO 16,17,22 respectivamente  de la raspberry Pi B+

```py
 sudo python ledsOn_3.py

```

Podemos observar que en listaGPIO tiene tres valor (16,17,22) estos representas las tres salidas GPIO de la Raspberry Pi
```py

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

```
_________________________________________________________________________

## ledsOn_alternos.py
#### Uso
La ejecución de este script encendera los LEDs numero 1,2  conectado a la GPIO 16,17 respectivamente  de forma alterna en la raspberry Pi B+

```py
 sudo python ledsOn_alternos.py

```

En este script se agrego una funcion que de forma simple entercala los valores de encendido y apgado para las GPIO 16 y 17, de igual forma se agrego un variable que almacena el tiempo en que se intercambain los valor.
```py
cT	      = 1 			# variable para almacenar el tiempo por defecto de 1 segundo


#--- Definicion de funciones
	.
	.
	.
def alternos(lista):			# Funcions para encender de forma alterna dos leds

    L.output(lista[0],L.HIGH)
    L.output(lista[1],L.LOW)
    time.sleep(cT)
    L.output(lista[0],L.LOW)
    L.output(lista[1],L.HIGH)
```
Para estos ejemplos listaGPIO se comporta como un Array[] de los que ya conocemos, es por esto que lista[0] contiene el valor '16' y lista[1] contiene el valor '17' 

_________________________________________________________________________

## ledsOn_alternosCiclo.py
#### Uso
La ejecución de este script encendera los LEDs numero 1,2  conectado a la GPIO 16,17 respectivamente  de forma alterna y por una candiad de ciclo en la raspberry Pi B+

```py
 sudo python ledsOn_alternosCiclo.py

```

Podemos ver que la funcion ciclosAlternos(lista, cCiclos,cCiclosMax) contiene un ciclo while el cual tiene un valor de ejecuacón entre cCiclos y cCiclosMax, estas  variables es donde se maneja la cantidad de veces que se repetira el ciclo, tambien muestra por pantalla el estado de las variables en cada ciclo

```py
def ciclosAlternos(lista, cCiclos,cCiclosMax): # Funcions para encender de forma alterna dos leds con un ciclo
    while cCiclos < cCiclosMax:
        L.output(lista[0],L.HIGH)
        L.output(lista[1],L.LOW)
        time.sleep(cT)
        L.output(lista[0],L.LOW)
        L.output(lista[1],L.HIGH)
        time.sleep(cT)
        cCiclos += 1				# incremento en 1 la variable cCiclos
        print "Ciclos Totales:" + str(cCiclosMax) + " ciclo Actual: " + str(cCiclos)        

```

La funcion ciclosAlternos() se invoca de esta forma, los valores de cCiclos=0 y cCiclosMas=5:

```py
	.
	.
	.
listaGPIO = [16,17]
cCiclos	  = 0               # variable para manejar el contador de ciclos de ejecucion
cCiclosMax = 5				# variable para manejar la cantidad  los ciclos de ejecucion
#--- Definicion de funciones
	.
	.
	.
#--- Ejecucion
ciclosAlternos(listaGPIO,cCiclos,cCiclosMax)
```

_________________________________________________________________________

## ledsOn_secuencias.py
#### Uso
La ejecución de este script encendera los LEDs numero 1,2,3,4,5,6  conectado a la GPIO 16,17,22,23,24,25 respectivamente  de forma secuencial

```py
 sudo python ledsOn_secuencias.py

```

el script ejecuta una funcion que enciende los LEDs de uno a la vez y apaga el estado anterior.
```py
def serieUnoLed(lista,cT=0.1):
    
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

```
 
_________________________________________________________________________

## ledsOn_secuenciasInv.py
#### Uso
La ejecución de este script encendera los LEDs numero 1,2,3,4,5,6  conectado a la GPIO 16,17,22,23,24,25 respectivamente  de forma secuencial y hace un juego de luces con la ejecucion de la funcion  serieUnoLed()
```py
 sudo python ledsOn_secuenciasInv.py

```

aca estan las dos fucniones de realizar el efecto de movimiento en los LEDs
```py
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
```

El llamado a estas funciones estan en el bloque de ejecucion
```py
#--- Ejecucion

iniGPIO(listaGPIO)

offTodo(listaGPIO)                               # se configuran todas las salidas definidas en listaGPIO

serieUnoLed(listaGPIO,cT)                       # se invoca la funcion que enciende de forma secuencial

serieUnoLedInv(listaGPIO,cT)                    # se invoca la funcion que enciende de forma secuencial Inv

time.sleep(2)                                   # detiene la ejecución por 2 segundos

L.cleanup()   

```










