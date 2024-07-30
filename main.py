import flet as ft
from Frontend import logo_screen, directorio, info, home_screen
import asyncio
import locale

def setup_screen(page : ft.Page):
    page.bgcolor = "#FFC5D9"
    page.adaptative= True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.locale_configuration = ft.LocaleConfiguration(current_locale=ft.Locale("es", "MX"))
    locale.setlocale(locale.LC_ALL, locale="es")
    page.scroll = ft.ScrollMode.ADAPTIVE
   
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
            ft.IconButton(ft.icons.PHONE, on_click=directorio_onclick), #Botón pantalla directorio
            ft.IconButton(ft.icons.BLUETOOTH, on_click=conexiones_onclick), #Botón pantalla conexiones
            ft.IconButton(ft.icons.ALARM, on_click=home_onclick), #Botón pantalla principal
            ft.IconButton(ft.icons.INFO, on_click=info_onclick), #Botón pantalla información
            ft.IconButton(ft.icons.VIDEO_CAMERA_BACK, on_click=video_onclick), #Botón pantalla videos
            ],
            alignment= ft.MainAxisAlignment.SPACE_EVENLY
        )        
    )
    
def directorio_onclick(e : ft.ControlEvent):
    e.page.controls.clear()
    directorio.main(e.page)
    

def conexiones_onclick(e):
    e.page.controls.clear()
    #TODO: Abrir screen conexiones
    print("Conexiones")

def home_onclick(e):
    e.page.controls.clear()
    #TODO: Abrir screen home
    print("Home")

def info_onclick(e):
    e.page.controls.clear()
    info.main(e.page)

def video_onclick(e):
    e.page.controls.clear()
    #TODO: Abrir screen video
    print("Video")
    
async def main(page: ft.Page):
    if page.platform.name == "WINDOWS":
        page.window.maximizable = False
        page.window.width = 350 #Ancho de la pantalla tani cambialo a 395  350
        page.window.height = 750 #Largo de la pantalla   750
        
    add_appbar(page)
    await logo_screen.main(page)    
    setup_screen(page)
    add_bottom_appbar(page)
    await home_screen.main(page)
    page.update()

asyncio.run(ft.app_async(target=main, name="FEMGUARD"))