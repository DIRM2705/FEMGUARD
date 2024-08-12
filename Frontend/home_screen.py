import flet as ft
import asyncio
from Utils.ble import BLE
from Utils import file

def main(page : ft.Page):
    ble = BLE.load_from_file()
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    
    name = ""
    try:
        name = file.load_user_data().name
    except FileNotFoundError:
        pass
    
    status_icon = ft.icons.CHECK if ble.is_connected else ft.icons.BLUETOOTH_DISABLED
    page.add(
        ft.Text(f"¡Hola {name}!", size=25, color="#CB568D", weight=ft.FontWeight.BOLD),
        ft.Icon(name=status_icon, color="#CB568D", size=150, tooltip="Estado de conexión"),
        ft.Text(f"Estado del collar: {get_conn_status(ble)}", color="#33313D", text_align=ft.TextAlign.CENTER)
    )
    
    page.update()


def get_conn_status(ble : BLE) -> str:
    return "Conectado" if ble.is_connected else "Desconectado"
#^^ 