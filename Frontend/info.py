import flet as ft

def add_labels(page: ft.Page):
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}','{tb5.value}'."
        page.update()

    t = ft.Text()
    tb1 = ft.TextField(label="Nombre")
    tb2 = ft.TextField(label="Apellidos")
    tb3 = ft.TextField(label="Celular")
    tb4 = ft.TextField(label="Tipo de sangre")
    page.add(tb1, tb2, tb3, tb4, t)
    
    page.add(
        ft.Dropdown(
            label="Día de nacimiento",
            hint_text="Selecciona tu día de nacimiento",
            options=[
                ft.dropdown.Option("1"),
                ft.dropdown.Option("2"),
                ft.dropdown.Option("3"),
                ft.dropdown.Option("4"),
                ft.dropdown.Option("5"),
                ft.dropdown.Option("6"),
                ft.dropdown.Option("7"),
                ft.dropdown.Option("8"),
                ft.dropdown.Option("9"),
                ft.dropdown.Option("10"),
                ft.dropdown.Option("11"),
                ft.dropdown.Option("12"),
                ft.dropdown.Option("13"),
                ft.dropdown.Option("14"),
                ft.dropdown.Option("15"),
                ft.dropdown.Option("16"),
                ft.dropdown.Option("17"),
                ft.dropdown.Option("18"),
                ft.dropdown.Option("19"),
                ft.dropdown.Option("20"),
                ft.dropdown.Option("21"),
                ft.dropdown.Option("22"),
                ft.dropdown.Option("23"),
                ft.dropdown.Option("24"),
                ft.dropdown.Option("25"),
                ft.dropdown.Option("26"),
                ft.dropdown.Option("27"),
                ft.dropdown.Option("28"),
                ft.dropdown.Option("29"),
                ft.dropdown.Option("30"),
                ft.dropdown.Option("31"),
            ],
            autofocus=True,
        )
    )
    page.add(
        ft.Dropdown(
            label="Mes de nacimiento",
            hint_text="Selecciona tu mes de nacimiento",
            options=[
                ft.dropdown.Option("Enero"),
                ft.dropdown.Option("Febrero"),
                ft.dropdown.Option("Marzo"),
                ft.dropdown.Option("Abril"),
                ft.dropdown.Option("Mayo"),
                ft.dropdown.Option("Junio"),
                ft.dropdown.Option("Julio"),
                ft.dropdown.Option("Agosto"),
                ft.dropdown.Option("Septiembre"),
                ft.dropdown.Option("Octubre"),
                ft.dropdown.Option("Noviembre"),
                ft.dropdown.Option("Diciembre"),
            ],
            autofocus=True,
            border_width=0.5
        )
    )
    tb5 = ft.TextField(label="Año de nacimiento")
    page.add(tb5, ft.Text("Ingresa tus 5 contactos de emergencia", size=12, weight=ft.FontWeight.W_900, selectable=True))
    tb6 = ft.TextField(label="Contacto 1")
    tb7 = ft.TextField(label="Contacto 2")
    tb8= ft.TextField(label="Contacto 3")
    tb9 = ft.TextField(label="Contacto 4")
    tb10 = ft.TextField(label="Contacto 5")
    page.add(tb6, tb7, tb8, tb9, tb10)
    

def main(page : ft.Page):
    add_labels(page)
    page.update()