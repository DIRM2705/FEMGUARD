import flet as ft

def main(page : ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    #boton de emergencia
    page.add(
        ft.IconButton( 
            icon=ft.icons.WARNING, 
            icon_color="white",
            icon_size=150,
            bgcolor="#CB568D",
            tooltip="Emergencia",
            padding=ft.padding.all(20)
        ),
    )

    page.update()

#^^ 