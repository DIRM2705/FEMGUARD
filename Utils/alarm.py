from Frontend import cancel_bttn, home_screen
import flet as ft
import asyncio
import winsdk.windows.devices.geolocation as wdg
from Utils import message, file

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
            user = file.load_user_data()
            await Alarm.ble.accept_alert()    
            try:
                async with asyncio.timeout(15):
                    await cancel_bttn.main(Alarm.ble, Alarm.app)
            except TimeoutError:
                #No se presionó el botón dentro de los 15 segundos
                Alarm.app.controls.clear()
                position = await Alarm.get_location()
                message.send_SOS_message(user.name, user.emergency_contacts, position)
                #print(position) #enviar mensaje
                home_screen.main(Alarm.app)
                await asyncio.sleep(25) #esperar 15 minutos
                await Alarm.ble.dismiss_alert()
                
    async def get_location() -> tuple[float, float]:
        '''
        Función que obtiene el geolocalizador del dipsositivo y luego retorna las coordenadas
        
        Retorna:    Una tupla con las coordenadas de la ubicación del dispositivo
        '''
        locator = wdg.Geolocator()
        try:
            pos = await locator.get_geoposition_async()
            return (pos.coordinate.latitude, pos.coordinate.longitude)
        except PermissionError as e:
            print(e)
    