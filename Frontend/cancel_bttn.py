import flet as ft
import asyncio
from Frontend import home_screen
from Utils.ble import BLE

ble : BLE = None
cancel_event = None

def set_ble(client : BLE):
    global ble
    ble = client

async def main(page : ft.Page):
    global cancel_event
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    title = ft.Text(value="DETENER ALARMA", color="Pink", weight=ft.FontWeight.BOLD, size=25)
    cancel_bttn = ft.IconButton(
        icon=ft.icons.FRONT_HAND,
        icon_color="White",
        icon_size=150,
        bgcolor="Red",
        tooltip="Detener alarma",
        on_click=cancel_on_click
    )
    
    await page.add_async(title, cancel_bttn)
    
    cancel_event = asyncio.Event()
    
    await cancel_event.wait()
    page.controls.clear()
    home_screen.main(page)

async def cancel_on_click(e):
    '''
        Función para cancelar la alarma, escribe en el canal de comunicación del collar el nivel de alerta como bajo
    '''
    global cancel_event, ble
    cancel_event.set()
    await ble.dismiss_alert()
    
    
    