import flet as ft

def main(page : ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    #boton de emergencia
    page.add(
        ft.IconButton( 
            icon=ft.icons.WARNING, 
                    icon_color="#CB568D",
                    icon_size=150,
                    tooltip="Emergencia",
        ),
    )

    page.update()

#^^ 