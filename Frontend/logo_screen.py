import flet as ft
from Utils.ble import BLE
from Utils.alarm import Alarm
from Exceptions.btExc import ConnectionUnsuccessfullException
from Utils import file

async def setup_ble_devices():
    ble = BLE.load_from_file() #Obtener cliente de archivo 
    
    if ble is None:
        ble = BLE(Alarm.panic, file.make_video)
        ble.save()
  
    Alarm.ble = ble
    try:
       await ble.connect_to_last_device()
       await ble.subscribe_to_alerts()     
    except ConnectionUnsuccessfullException as e:
        print(e)

async def main(page: ft.Page):
    page.bgcolor = "White"
    img = ft.Image(
        src=f"images/FEMGUARD LOGO.png",
        width=225,
        height=225,
        fit=ft.ImageFit.CONTAIN,
    )
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 

    page.add(img)
    page.update()
    
    Alarm.app = page
    
    await setup_ble_devices()
