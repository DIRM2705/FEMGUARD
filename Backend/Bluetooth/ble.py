from bleak import BleakScanner, BleakClient, BLEDevice, AdvertisementData, BleakGATTCharacteristic
import asyncio

async def get_nearby_devices() -> list[BLEDevice]:
    scanner = BleakScanner()
    correct_nearby_devices = set()
    
    #buscar los dispositivos cercanos, guardando datos de advertising
    discoveries = await scanner.discover(timeout=10, return_adv=True)
    
    #Añadir a la lista solo los dispostivos que tengan los servicios correctos
    for device, adv_data in discoveries.values():
        if data_contains_inmediate_alert_UUID(adv_data):
            correct_nearby_devices.add(device)
        
    return correct_nearby_devices
    
def data_contains_inmediate_alert_UUID(adv_data : AdvertisementData) -> bool:
    IMMEDIATE_ALERT_UUID = "00001802-0000-1000-8000-00805f9b34fb" #Obtenido de documento bt "Assigned numbers"
    return IMMEDIATE_ALERT_UUID in adv_data.service_uuids
    
    
async def connect_to_device(device : BLEDevice) -> BleakClient:
    client = BleakClient(device)
    await client.connect()
    return client
    
async def subscribe_to_alert(client : BleakClient):
    ALERT_LEVEL_CHAR = 8
    await client.start_notify(ALERT_LEVEL_CHAR, callback)
    
#Función de callback demo
def callback(sender: BleakGATTCharacteristic, data: bytearray):
    print(f"{sender}: {data}")
    
    
async def demo():
    devices = await get_nearby_devices()
    if len(devices) > 0:
        for device in devices:
            client = await connect_to_device(device)
            break
        
        await subscribe_to_alert(client)
        await asyncio.sleep(180)


asyncio.run(demo())