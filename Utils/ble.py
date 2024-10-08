from bleak import BleakScanner, BleakClient, BLEDevice, AdvertisementData
from bleak.exc import BleakDeviceNotFoundError
from Utils.file import save_ble_client, load_ble_client
from Exceptions.btExc import *

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
    _UART_TX_UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    
    def __init__(self, panic_function, vid_function):
        '''
        Constructor de clase, inicializa:
            - Cliente bluetooth
            - Diccionario de dispositivos cercanos
            - Función a ejecutar al recibir la alerta
            
        Parámetros:     panic_fuction: La función que debe llamarse cuando se obtiene una señal de alarma
                        vid_function: La función que debe llamarse cuando se reciben datos de video
        '''
        self._client = None
        self._nearby_devices = dict()
        self._panic_function = panic_function
        self._make_vid_function = vid_function
        self.is_connected = False
    
    def on_disconnect(callback):
        data = load_ble_client()
        data.is_connected = False
        save_ble_client(data)
        
    def load_from_file():
        '''
        Carga un cliente BLE desde un archivo para una conexión rápida,
        si no existiera el archivo o hubiera un problema crea un cliente vacio
        '''
        
        try:
            bleData : BLEData = load_ble_client()
            ble = BLE(bleData.panic, bleData.vid)
            ble._client = BleakClient(bleData.client_name, disconnected_callback=BLE.on_disconnect) 
            ble.is_connected = bleData.is_connected 
            return ble     
        except Exception as e:
            print(e)
            return None       
            
    
    def save(self):
        client = self._client.address if self._client is not None else ""
        data = BLEData(client, self._panic_function, self._make_vid_function, self.is_connected)
        save_ble_client(data)
        
        
    async def get_nearby_devices(self) -> list[str]:
        '''
        Escanea los dispositivos cercanos y crea el diccionario de los dispositivos
        que cumplen con los requerimientos preestablecidos
            
        Retorna: Una lista con los nombres de los dispositivos del diccionario
        '''
        scanner = BleakScanner()
        self._nearby_devices.clear()
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
                self._nearby_devices[device.name] = device.address
        
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
            self._client = BleakClient(device, disconnected_callback=BLE.on_disconnect)
            await self._client.connect()
            self.is_connected = True
        except KeyError:
            raise ConnectionUnsuccessfullException("Nombre del dispositivo incorrecto")
        except BleakDeviceNotFoundError:
            raise ConnectionUnsuccessfullException("Dispositivo no encontrado")
    
    async def connect_to_last_device(self):
        '''
        Conecta el cliente bluetooth al último dispositivo seleccionado
        Se espera utilizar esta función al iniciar la app para reconectar el collar automáticamente
        '''
        
        if self._client is None or self._client.address == "":
            raise ConnectionUnsuccessfullException("El cliente no tiene conexiones previas")
        try:
            await self._client.connect()
            self.is_connected = True
            self.save()
        except AttributeError:
            raise ConnectionUnsuccessfullException("El cliente no tiene conexiones previas")
        except BleakDeviceNotFoundError:
            raise ConnectionUnsuccessfullException("Dispositivo no encontrado")
    
    async def subscribe_to_alerts(self):
        '''
        Pone al cliente a la espera de que el dispositivo conectado envíe notificaciones de alerta inmediata
        o reciba datos del sensor de cámara
        '''
        await self._client.start_notify(self._ALERT_LEVEL_UUID, self._panic_function)
        await self._client.start_notify(self._UART_TX_UUID, self._make_vid_function)
 
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
    
    async def accept_alert(self):
        '''
        Avisa al collar que la alerta ha sido recibida y puede empezar a mandar datos
        '''
        await self._client.write_gatt_char(self._ALERT_LEVEL_UUID, data=b"Accept Alert", response=False)
        
class BLEData:
    def __init__(self, client : str, panic_func, vid_func, connected : bool) -> None:
        self.client_name = client 
        self.panic = panic_func
        self.vid = vid_func  
        self.is_connected = connected
            