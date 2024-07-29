import flet as ft

def main(page: ft.Page):
    img = ft.Image(
        src=f"images/FEMGUARD LOGO.png",
        width=225,
        height=225,
        fit=ft.ImageFit.CONTAIN,
    )
    page.vertical_alignment=ft.MainAxisAlignment.CENTER 
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER 

    page.add(img)
    page.update()
