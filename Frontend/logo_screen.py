import flet as ft
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

def main(page: ft.Page):
    img = ft.Image(
        src=f"images/FEMGUARD LOGO.png",
        width=225,
        height=225,
        fit=ft.ImageFit.CONTAIN,
    )
    setup_screen(page)
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 

    page.add(img)
    add_appbar(page)
    page.update()
