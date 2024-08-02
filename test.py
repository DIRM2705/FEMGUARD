from Utils.ble import BLE
from Utils.alarm import Alarm
from Utils import file
from Exceptions.btExc import ConnectionUnsuccessfullException
import asyncio

async def main():
    ble = BLE(Alarm.panic, file.make_video) #Obtener de archivo
    Alarm.ble = ble
    try:
        # await ble.connect_to_last_device()
        await ble.get_nearby_devices()
        await ble.connect_to_device("FEMGUARD")
        for value in ble._client.services.characteristics.values():
            print(value.uuid)
        await ble.subscribe_to_alerts()       
    except ConnectionUnsuccessfullException as e:
        print(e)
        
asyncio.run(main())
asyncio.run(asyncio.sleep(60))