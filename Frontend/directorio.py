import flet as ft

def main(page : ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.add(
        ft.Text("NÚMEROS PARA EMERGENCIAS", size=14, weight=ft.FontWeight.W_900, selectable=True, color="#33313D"),
        ft.Text("Marcación rápida de auxilio", size=10, color="#33313D"),
        ft.TextButton("Emergencia Nivel Nacional(911)", icon="EMERGENCY", icon_color="red"),
        ft.TextButton("Línea mujer, apoyo psicoógico y legal", icon="SUPPORT_AGENT",icon_color="pink"),
        ft.TextButton("Seguridad pública", icon="SECURITY",icon_color="green"),
        ft.Text("CONTACTO CON FEMGUARD", size=12, weight=ft.FontWeight.W_900, selectable=True, color="#33313D"),
        ft.TextButton("WhatsApp", icon="MESSAGE",icon_color="green"),
        ft.TextButton("Correo electrónico", icon="EMAIL",icon_color="#000000"),
    )
    page.update()