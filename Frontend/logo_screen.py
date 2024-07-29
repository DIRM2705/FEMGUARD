import flet as ft
from Utils.ble import BLE
from Exceptions.btExc import ConnectionUnsuccessfullException

async def setup_ble_devices():
    ble = BLE() #Obtener de archivo
    try:
        await ble.connect_to_last_device()
    except ConnectionUnsuccessfullException as e:
        print(e)
        pass

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
    
    await setup_ble_devices()
