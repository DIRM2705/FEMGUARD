import flet as ft
from Frontend import logo_screen, directorio, info, home_screen, video, bluetooth
import asyncio
import locale
from Utils.ble import BLE

def setup_screen(page : ft.Page):
    page.bgcolor = "#FFFFFF"
    page.adaptative= True
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.locale_configuration = ft.LocaleConfiguration(current_locale=ft.Locale("es", "MX"))
    locale.setlocale(locale.LC_ALL, locale="es")
    page.scroll = ft.ScrollMode.ADAPTIVE
   
def add_appbar(page : ft.Page):
    page.appbar = ft.AppBar(
        bgcolor="#E1BFD0", #Color de la barra superior
        toolbar_height=40, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5))
    
def add_bottom_appbar(page : ft.Page):
    bttn_row = ft.Row(
            controls=[
            ft.IconButton(ft.icons.CALL,icon_color="#DC92B5", on_click=directorio_onclick),#boton contactos
            ft.IconButton(ft.icons.BLUETOOTH,icon_color="#DC92B5", on_click=conexiones_onclick), #Botón pantalla conexiones
            ft.IconButton(ft.icons.HOME,icon_color="#CB568D", on_click=home_onclick), #Botón pantalla principal
            ft.IconButton(ft.icons.BADGE,icon_color="#DC92B5", on_click=info_onclick), #Botón pantalla información
            ft.IconButton(ft.icons.LINKED_CAMERA,icon_color="#DC92B5", on_click=video_onclick), #Botón pantalla videos
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    page.bottom_appbar = ft.BottomAppBar(
        bgcolor="white",
        content= ft.Column(
            controls=[
                ft.Divider(color="#E1BFD0"),
                bttn_row
                ]
            )   
    )
    
def directorio_onclick(e : ft.ControlEvent):
    e.page.controls.clear()
    directorio.main(e.page)
    

async def conexiones_onclick(e):
    e.page.controls.clear()
    await bluetooth.main(e.page)

def home_onclick(e):
    e.page.controls.clear()
    home_screen.main(e.page)

def info_onclick(e):
    e.page.controls.clear()
    info.main(e.page)

def video_onclick(e):
    e.page.controls.clear()
    video.main(e.page)
    
def config_for_pc(page : ft.Page):
    if page.platform.name == "WINDOWS":
        page.window.maximizable = False
        page.window.width = 350 #Ancho de la pantalla tani cambialo a 395  350
        page.window.height = 750 #Largo de la pantalla   750
    
async def main(page: ft.Page):
    config_for_pc(page)
    add_appbar(page)
    await logo_screen.main(page)    
    setup_screen(page)
    add_bottom_appbar(page)
    page.controls.clear()
    home_screen.main(page)
    page.update()

asyncio.run(ft.app_async(target=main, name="FEMGUARD"))