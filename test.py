from Utils.ble import BLE
import asyncio

async def main():
    ble = BLE()
    await ble.get_nearby_devices()
    await ble.connect_to_device("FEMGUARD")
    await ble.subscribe_to_alerts()

asyncio.run(main())
    
    