import datetime
import flet as ft

def setup_screen(page : ft.Page):
    page.window.maximizable = False
    page.window.width = 300 #Ancho de la pantalla
    page.window.height = 500 #Largo de la pantalla
    page.bgcolor = '#FFC5D9'
    
def add_bars(page : ft.Page):
    page.bottom_appbar = _get_appbar()
    page.appbar = ft.AppBar(
        bgcolor='#8A5D86', #Color de la barra superior
        toolbar_height=25, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5)) #Cambiar radio para cambiar cuanto se redondea la barra superior

def _get_appbar() -> ft.BottomAppBar:
    return ft.BottomAppBar(
        bgcolor="White",
        content= ft.Row(controls=[
            ft.IconButton(ft.icons.PHONE), #Botón pantalla directorio
            ft.IconButton(ft.icons.BLUETOOTH), #Botón pantalla conexiones
            ft.IconButton(ft.icons.ALARM), #Botón pantalla principal
            ft.IconButton(ft.icons.INFO), #Botón pantalla información
            ft.IconButton(ft.icons.VIDEO_CAMERA_BACK), #Botón pantalla videos
        ])        
    )


def fecha(page: ft.Page):

    def handle_change(e):
        page.add(ft.Text(f"Fecha de nacimiento: {e.control.value.strftime('%Y-%m-%d')}"))

    page.add(
        ft.ElevatedButton(
            "Selecciona tu fecha de nacimiento",
            icon=ft.icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=1900, month=1, day=1),
                    last_date=datetime.datetime(year=2024, month=12, day=31),
                    on_change=handle_change,
                    
                )
            ),
        )
    )



def main(page : ft.Page):
    setup_screen(page)
    page.locale_configuration.supported_locales = [Locale("es", "MX")] 
    page.locale_configuration.current_locale = Locale("es", "MX")
    fecha(page)
    #Quitar para la splash screen
    add_bars(page)
    page.update()
    
    

    
ft.app(target=main)