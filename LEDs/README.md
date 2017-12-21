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




