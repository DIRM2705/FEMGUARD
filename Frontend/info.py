import flet as ft
import calendar
import datetime


def add_labels(page: ft.Page):
    tipos_de_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    tb1 = ft.TextField(label="Nombre")
    tb2 = ft.TextField(label="Apellidos")
    tb3 = ft.TextField(label="Celular")
    tb4 = ft.Dropdown(
            label="Tipo de sangre",
            options=[ft.dropdown.Option(x) for x in tipos_de_sangre],
        )
    page.add(tb1, tb2, tb3, tb4)
    
    
def add_birthdate_sel(page : ft.Page):
    def on_month_year_change(e):
        year = actual_year if not year_dropdown.value else int(year_dropdown.value)
        month = list(calendar.month_abbr).index(month_dropdown.value)
        day_dropdown.options = [ft.dropdown.Option(i) for i in range(1, calendar.monthrange(year, month)[1] + 1)]
        page.update()
        
    actual_year = datetime.date.today().year
    control_width = page.width/3.5
    
    day_dropdown = ft.Dropdown(
            label="Día",
            options=[ft.dropdown.Option(i) for i in range (1, 32)],
            width=control_width
        )
    
    month_dropdown = ft.Dropdown(
            label="Mes",
            options=[ft.dropdown.Option(calendar.month_abbr[i]) for i in range(1, 13)],
            on_change=on_month_year_change,
            width=control_width
        )
    
    year_dropdown = ft.Dropdown(
            label="Año",
            options=[ft.dropdown.Option(i) for i in range(actual_year, actual_year - 80, -1)],
            on_change=on_month_year_change,
            width=control_width
        )
    
    selector = ft.Row(
        controls=[day_dropdown, month_dropdown, year_dropdown],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    page.add(ft.Text("Fecha de nacimiento"), selector)
    
def add_contacts(page : ft.Page):
    page.add(ft.Text("Ingresa tus 5 contactos de emergencia", size=12, weight=ft.FontWeight.W_900))
    tb6 = ft.TextField(label="Contacto 1")
    tb7 = ft.TextField(label="Contacto 2")
    tb8= ft.TextField(label="Contacto 3")
    tb9 = ft.TextField(label="Contacto 4")
    tb10 = ft.TextField(label="Contacto 5")
    page.add(tb6, tb7, tb8, tb9, tb10)

def main(page : ft.Page):
    add_labels(page)
    add_birthdate_sel(page)
    add_contacts(page)
    page.update()