from bleak import BleakGATTCharacteristic
from Bluetooth.ble import BLE
import asyncio
from asyncio.exceptions import TimeoutError

_HIGH_ALERT_MSSG = "High Alert"

async def panic(sender : BleakGATTCharacteristic, data : bytearray):
    '''
    Función que se debe llamar cuando al recibir la alerta inmediata del collar indicando que hay una emergencia.
    Espera 15 segundos antes de cerrar la pantalla del botón cancelar y 
    comenzar a realizar las acciones de seguridad
    '''
    if data.decode() == _HIGH_ALERT_MSSG:    
        try:
            task = asyncio.create_task(cancelation_bttn_task())
            await asyncio.wait_for(task, timeout=15)
        except TimeoutError:
            #No se presionó el botón dentro de los 15 segundos
            print("La grabación comenzó")
            print("Notificar contactos")
            
async def cancelation_bttn_task():
    print("Cancelation task")
    #TODO: llamar a abrir pantalla del botón
            
def cancel_alarm(ble : BLE):
    '''
    Función para cancelar la alarma, escribe en el canal de comunicación del collar el nivel de alerta como bajo,
    abre la pantalla inicial y cierra la pantalla del botón cancelar
    
    Parámetros:     ble - El cliente bluetooth de la app
    '''
    print("Alarma cancelada")
    