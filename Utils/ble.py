from bleak import BleakScanner, BleakClient, BLEDevice, AdvertisementData, BleakGATTCharacteristic
from bleak.exc import BleakDeviceNotFoundError
from Exceptions.btExc import *
import asyncio
from asyncio.exceptions import TimeoutError

class BLE :
    '''
    Cliente bluetooth low energy de la aplicación.
        - Busca dispositivos cercanos,
        - Conecta con dispositivos BLE que cumplan las características:
            - Tienen la UUID de alerta inmediata
        - Se suscribe a las notificaciones enviadas por el dispositivo de seguridad
    '''
    #constantes de clase
    _IMMEDIATE_ALERT_UUID = "00001802-0000-1000-8000-00805f9b34fb"
    _ALERT_LEVEL_UUID = "00002a06-0000-1000-8000-00805f9b34fb"
    
    def __init__(self):
        '''
        Constructor de clase, inicializa:
            - Cliente bluetooth
            - Diccionario de dispositivos cercanos
            - Función a ejecutar al recibir la alerta
        '''
        self._client = None
        self._nearby_devices = dict()

    async def panic_function(sender : BleakGATTCharacteristic, data : bytearray):
        '''
        Función que se debe llamar cuando al recibir la alerta inmediata del collar indicando que hay una emergencia.
        Espera 15 segundos antes de cerrar la pantalla del botón cancelar y 
        comenzar a realizar las acciones de seguridad
        '''
        HIGH_ALERT_MSSG = "High Alert"
        
        if data.decode() == HIGH_ALERT_MSSG:    
            try:
                task = asyncio.create_task()
                await asyncio.wait_for(task, timeout=15)
            except TimeoutError:
                #No se presionó el botón dentro de los 15 segundos
                print("La grabación comenzó")
                print("Notificar contactos")
        
    async def get_nearby_devices(self) -> list[str]:
        '''
        Escanea los dispositivos cercanos y crea el diccionario de los dispositivos
        que cumplen con los requerimientos preestablecidos
            
        Retorna: Una lista con los nombres de los dispositivos del diccionario
        '''
        scanner = BleakScanner()
        
        #buscar los dispositivos cercanos, guardando datos de advertising
        discoveries = await scanner.discover(timeout=10, return_adv=True)
        self._create_filtered_devices_dic_from(discoveries.values())
        
        #retorna una lista con los nombres de los dispositivos cercanos
        return self._nearby_devices.keys()
    
    def _create_filtered_devices_dic_from(self, discoveries : tuple[BLEDevice, AdvertisementData]):
        '''
        Guarda en el diccionario de dispositivos cercanos,
        los dispositivos que cumplen con las características preestablecidas
            
        Parámetros:     discoveries: una tupla que contenga el objeto representativo
                        de blake.BLEDevice y los datos de anuncio del dispositivo
        '''
        for device, adv_data in discoveries:
            #Verificar que contenga UUID de alerta inmediata
            if self._data_contains_inmediate_alert_UUID(adv_data):
                self._nearby_devices[device.name] = device
        
    def _data_contains_inmediate_alert_UUID(self, adv_data : AdvertisementData) -> bool: 
        '''
        Devuelve si los datos del dispositivo contienen la UUUID de alerta inmediata
        
        Parámetros:     adv_data: Los datos de anuncio del dispositivo que se evalua
        
        Retorna:        Verdadero si los datos contienen la UUID de alerta inmediata
        '''
        return self._IMMEDIATE_ALERT_UUID in adv_data.service_uuids
    
    async def connect_to_device(self, device_name : str):
        '''
        Conecta el cliente bluetooth al dispositivo seleccionado
        
        Parámetros:     device_name: El nombre del dispositivo al que se quiere conectar
        '''
        try:
            device = self._nearby_devices[device_name]
            self._client = BleakClient(device)
            await self._client.connect()
        except KeyError:
            raise ConnectionUnsuccessfullException("Nombre del dispositivo incorrecto")
        except BleakDeviceNotFoundError:
            raise ConnectionUnsuccessfullException("Dispositivo no encontrado")
    
    async def connect_to_last_device(self):
        '''
        Conecta el cliente bluetooth al último dispositivo seleccionado
        Se espera utilizar esta función al iniciar la app para reconectar el collar automáticamente
        '''
        try:
            await self._client.connect()
        except AttributeError:
            raise ConnectionUnsuccessfullException("El cliente no tiene conexiones previas")
        except BleakDeviceNotFoundError:
            raise ConnectionUnsuccessfullException("Dispositivo no encontrado")
    
    async def subscribe_to_alert(self):
        '''
        Pone al cliente a la espera de que el dispositivo conectado envíe notificaciones de alerta inmediata
        '''
        await self._client.start_notify(self._ALERT_LEVEL_UUID, BLE.panic_function)
 
    async def dismiss_alert(self):
        '''
        Cambia el nivel de alerta a "No alert" en el dispositivo conectado
        '''
        await self._client.write_gatt_char(self._ALERT_LEVEL_UUID, data=b"No Alert", response=False)
 
    def has_devices(self) -> bool:
        '''
        Revisa si el cliente tiene dispositivos cercanos
        
        Retorna: Verdadero si hay al menos un dispositivo cercano
        '''   
        
        return len(self._nearby_devices) > 0