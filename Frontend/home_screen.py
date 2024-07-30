import flet as ft

def setup_screen(page : ft.Page):
    page.window.maximizable = False
    page.window.width = 300 #Ancho de la pantalla
    page.window.height = 500 #Largo de la pantalla
    page.bgcolor = "White"
    
def add_bars(page : ft.Page):
    page.bottom_appbar = _get_appbar()
    page.appbar = ft.AppBar(
        bgcolor="#E1BFD0", #Color de la barra superior
        toolbar_height=40, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5)) #Cambiar radio para cambiar cuanto se redondea la barra superior

def _get_appbar() -> ft.BottomAppBar:
    return ft.BottomAppBar(
        bgcolor="White",
        content= ft.Row(controls=[
            ft.IconButton(ft.icons.CALL,icon_color="#DC92B5"),#boton contactos
            ft.IconButton(ft.icons.BLUETOOTH,icon_color="#DC92B5"), #Botón pantalla conexiones
            ft.IconButton(ft.icons.HOME,icon_color="#CB568D"), #Botón pantalla principal
            ft.IconButton(ft.icons.BADGE,icon_color="#DC92B5"), #Botón pantalla información
            ft.IconButton(ft.icons.LINKED_CAMERA,icon_color="#DC92B5"), #Botón pantalla videos
        ])        
    )

def main(page : ft.Page):
    setup_screen(page)
    add_bars(page)
    #boton de emergencia
    page.add(
        ft.IconButton( 
            icon=ft.icons.WARNING, 
                    icon_color="#CB568D",
                    icon_size=150,
                    tooltip="Emergencia",
        ),
    )
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    page.update()

#^^ 