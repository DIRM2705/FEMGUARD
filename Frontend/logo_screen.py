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
        shape=ft.RoundedRectangleBorder(radius=3.5)) #Cambiar radio para cambiar cuanto se redondea la barra superior

def main(page: ft.Page):
    page.bgcolor = "white"
    page.padding=0
    page.adaptative= True


    img = ft.Image(
        src=f"C:/Users/whyga/Downloads/Image (1).png",
        width=225,
        height=225,
        fit=ft.ImageFit.CONTAIN,
    )
    setup_screen(page)
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 

    page.add(img)
    add_bars(page)
    page.update()
ft.app(target=main)
