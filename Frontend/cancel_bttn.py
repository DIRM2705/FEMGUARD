import flet as ft
import asyncio

def main(page : ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    title = ft.Text(value="DETENER ALARMA", color="Pink", weight=ft.FontWeight.BOLD, size=25)
    cancel_bttn = ft.IconButton(
        icon=ft.icons.FRONT_HAND,
        icon_color="White",
        icon_size=150,
        bgcolor="Red",
        tooltip="Detener alarma"
    )
    
    page.add(title, cancel_bttn)
    
ft.app(main)
    
async def panic_function(sender, data : bytearray):
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