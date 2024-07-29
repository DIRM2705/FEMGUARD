import flet as ft
from Frontend import logo_screen
import asyncio

def setup_screen(page : ft.Page):
    page.bgcolor = "#FFC5D9"
    page.padding=0
    page.adaptative= True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.locale_configuration = ft.LocaleConfiguration(current_locale=ft.Locale("es", "MX"))
   
def add_appbar(page : ft.Page):
    page.appbar = ft.AppBar(
        bgcolor="#E1BFD0", #Color de la barra superior
        toolbar_height=35, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5)) #Cambiar radio para cambiar cuanto se redondea la barra superior
    
def add_bottom_appbar(page : ft.Page):
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="White",
        content= ft.Row(
            controls=[
            ft.IconButton(ft.icons.PHONE), #Botón pantalla directorio
            ft.IconButton(ft.icons.BLUETOOTH), #Botón pantalla conexiones
            ft.IconButton(ft.icons.ALARM), #Botón pantalla principal
            ft.IconButton(ft.icons.INFO), #Botón pantalla información
            ft.IconButton(ft.icons.VIDEO_CAMERA_BACK), #Botón pantalla videos
            ],
            alignment= ft.MainAxisAlignment.SPACE_EVENLY
        )        
    )
    
async def main(page: ft.Page):
    if page.platform.name == "WINDOWS":
        page.window.maximizable = False
        page.window.width = 350 #Ancho de la pantalla tani cambialo a 395  350
        page.window.height = 750 #Largo de la pantalla   750
        
    add_appbar(page)
    await logo_screen.main(page)    
    setup_screen(page)
    add_bottom_appbar(page)
    page.update()
    

asyncio.run(ft.app_async(target=main))