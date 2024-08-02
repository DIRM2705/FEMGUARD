from Frontend import cancel_bttn, home_screen
import flet as ft
import asyncio

class Alarm:
    def __init__(self, ble, cancel_screen : ft.Page) -> None:
        '''
        Alarma para comenzar la secuencia de pánico en emergencia, notifica contactos y recibe datos de la cámara
        
        Parámetros:     ble: El cliente bluetooth de la app
        '''
        Alarm.app = cancel_screen
        Alarm.ble = ble
        
    async def panic(sender, data : bytearray):
        '''
        Función que se debe llamar cuando al recibir la alerta inmediata del collar indicando que hay una emergencia.
        Espera 15 segundos antes de cerrar la pantalla del botón cancelar y 
        comenzar a realizar las acciones de seguridad
        '''
        
        HIGH_ALERT_MSSG = "High Alert"
            
        if data.decode() == HIGH_ALERT_MSSG:
            await Alarm.ble.accept_alert()    
            try:
                async with asyncio.timeout(15):
                    await cancel_bttn.main(Alarm.ble, Alarm.app)
            except TimeoutError:
                #No se presionó el botón dentro de los 15 segundos
                Alarm.app.controls.clear()
                home_screen.main(Alarm.app)
                print("La grabación comenzó")
                print("Notificar contactos")
                await asyncio.sleep(25) #esperar 15 minutos
                await Alarm.ble.dismiss_alert()
    