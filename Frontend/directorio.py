import flet as ft

def main(page : ft.Page):
    page.add(
        ft.Text("NÚMEROS PARA EMERGENCIAS", size=14, weight=ft.FontWeight.W_900, selectable=True),
        ft.Text("Marcación rápida de auxilio", size=10),
        ft.TextButton("Emergencia Nivel Nacional(911)", icon="EMERGENCY", icon_color="red"),
        ft.TextButton("Línea mujer, apoyo psicoógico y legal", icon="SUPPORT_AGENT",icon_color="pink"),
        ft.TextButton("Seguridad pública", icon="SECURITY",icon_color="green"),
        ft.Text("CONTACTO CON FEMGUARD", size=12, weight=ft.FontWeight.W_900, selectable=True),
        ft.TextButton("Llamar", icon="CONTACT_PHONE", icon_color="blue"),
        ft.TextButton("WhatsApp", icon="MESSAGE",icon_color="green"),
        ft.TextButton("Correo electrónico", icon="EMAIL",icon_color="#000000"),
    )
    page.update()
    
ft.app(target=main)