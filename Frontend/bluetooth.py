import flet as ft
def setup_screen(page : ft.Page):
    page.window.maximizable = False
    page.window.width = 300 #Ancho de la pantalla tani cambialo a 395  350
    page.window.height = 500 #Largo de la pantalla   750
    page.bgcolor = "White"

def add_bars(page : ft.Page):
    page.appbar = ft.AppBar(
        bgcolor="#E1BFD0", #Color de la barra superior
        toolbar_height=35, #Altura de la barra superior
        shape=ft.RoundedRectangleBorder(radius=3.5))

def main(page: ft.Page):
    page.bgcolor = "white"
    page.padding=0
    page.adaptative= True
    add_bars(page)
    setup_screen(page)
    page.add(
         ft.ElevatedButton(
            adaptive=True,
            bgcolor="#F9E7F1",
            width=page.width,
            height=50,
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SIGNAL_CELLULAR_ALT, color="blue"),
                    ft.Text("Unnamed"),
                ], 
                tight=True,
            ),
         ), 
         ft.ElevatedButton(
            adaptive=True,
            bgcolor="#F9E7F1",
            width=page.width,
            height=50, 
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SIGNAL_CELLULAR_ALT, color="blue"),
                    ft.Text("Unnamed"),
                ], 
                tight=True,
            ),
         ), 
         ft.ElevatedButton (
            adaptive=True,
            bgcolor="#F9E7F1",
            width=page.width,
            height=50, 
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SIGNAL_CELLULAR_ALT, color="blue"),
                    ft.Text("Unnamed"),
                ], 
                tight=True,
            ),
         ), 
         ft.ElevatedButton(
            adaptive=True,
            bgcolor="#F9E7F1",
            width=page.width,
            height=50, 
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.SIGNAL_CELLULAR_ALT, color="blue"),
                    ft.Text("Unnamed"),
                ], 
                tight=True,
            ),
         )

    
    )
    page.update()

ft.app(target=main)

