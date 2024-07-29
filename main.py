import flet as ft
from Utils.ble import BLE
from Frontend import directorio, logo_screen
from Exceptions.btExc import ConnectionUnsuccessfullException
import asyncio

async def setup_ble_devices():
    ble = BLE() #Obtener de archivo
    try:
        await ble.connect_to_last_device()
    except ConnectionUnsuccessfullException as e:
        pass

def setup_screen(page : ft.Page):
    page.window.maximizable = False
    page.window.width = 350 #Ancho de la pantalla tani cambialo a 395  350
    page.window.height = 750 #Largo de la pantalla   750
    page.bgcolor = "White"
    page.padding=0
    page.adaptative= True
    
def add_appbar(page : ft.Page):
    page.appbar = ft.AppBar(
        bgcolor="#E1BFD0", #Color de la barra superior
        toolbar_height=35, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5)) #Cambiar radio para cambiar cuanto se redondea la barra superior
    
async def main(page: ft.Page):
    setup_screen(page)
    add_appbar(page)
    await logo_screen.main(page)
    

asyncio.run(ft.app_async(target=main))