import flet as ft
import calendar
import datetime
from Utils.file import save_user_data, load_user_data
from user import UserData


def add_labels(page: ft.Page, user : UserData):
    tipos_de_sangre = ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"]
    
    def on_name_change(e):
        no_space_val = name_box.value.replace(" ", "")
        if not no_space_val.isalpha() or not no_space_val:
            show_error_message(page, "Coloca tu nombre como aparece en tus documentos oficiales")
            name_box.value = user.name
            page.update()
        update_user_field(user, "name", name_box.value)
        
    def on_phone_change(e):
        new_val = phone_box.value.replace(" ", "")
        if len(new_val) != 10 or not new_val.isdecimal():
            show_error_message(page, "Número de teléfono no válido")
            phone_box.value = user.phone_number
            page.update()
            return
        update_user_field(user, "phone", new_val)
        
    def on_blood_change(e):
        update_user_field(user, "blood", blood_box.value)
        
    def on_height_change(e):
        try:
            new_val = int(height_box.value)
            if new_val < 0 or new_val > 300:
                show_error_message(page, "Altura no válida")
                height_box.value = user.height
                page.update()
                return
            update_user_field(user, "height", new_val)
        except ValueError:
            show_error_message(page, "Coloque su altura en centímetros")
            height_box.value = user.height
            page.update()
            return
        
    def on_weight_change(e):
        try:
            new_val = float(weight_box.value)
            if new_val < 0:
                show_error_message(page, "Peso no válido")
                weight_box.value = user.weigth
                page.update()
                return
            update_user_field(user, "weight", new_val)
        except ValueError:
            show_error_message(page, "Coloque su peso en kilogramos")
            weight_box.value = user.weigth
            page.update()
            return
        
    
    name_box = ft.TextField(label="Nombre", value=user.name, on_blur=on_name_change, color="#33313D", label_style=ft.TextStyle(color="#D0D0D0"), border_color="#CC92AF")
    phone_box = ft.TextField(label="Celular", value=user.phone_number, on_blur=on_phone_change, color="#33313D", label_style=ft.TextStyle(color="#D0D0D0"), border_color="#CC92AF")
    blood_box = ft.Dropdown(
            label="Tipo de sangre",
            options=[ft.dropdown.Option(x) for x in tipos_de_sangre],
            value=user.blood_type,
            on_change=on_blood_change,
            color="#33313D",
            label_style=ft.TextStyle(color="#D0D0D0"),
            border_color="#CC92AF"
        )
    
    height_box = ft.TextField(label="Estatura", value=user.height, width=page.width/1.25, on_blur=on_height_change, color="#33313D", label_style=ft.TextStyle(color="#D0D0D0"), border_color="#CC92AF")
    
    height_row = ft.Row(
        controls=[
            height_box,
            ft.Text("cm", color="#33313D")
        ]
    )
    
    weight_box = ft.TextField(label="Peso", value=user.weigth, width=page.width/1.25, on_blur=on_weight_change, color="#33313D", label_style=ft.TextStyle(color="#D0D0D0"), border_color="#CC92AF")
    
    weight_row = ft.Row(
        controls=[
            weight_box,
            ft.Text("kg", color="#33313D")
        ]
    )
    
    page.add(name_box, phone_box, blood_box, height_row, weight_row)
       
def add_birthdate_sel(page : ft.Page, user : UserData):
    actual_year = datetime.date.today().year
    control_width = page.width/3.5
    
    def update_birthdate(e):
        try:
            day = int(day_dropdown.value)
            month = list(calendar.month_abbr).index(month_dropdown.value)
            year = int(year_dropdown.value)
            date = datetime.date(year, month, day)
            update_user_field(user, "birth", date)
        except ValueError:
            pass

    def on_month_year_change(e):
        year = actual_year if not year_dropdown.value else int(year_dropdown.value)
        month = list(calendar.month_abbr).index(month_dropdown.value)
        day_dropdown.options = [ft.dropdown.Option(i) for i in range(1, calendar.monthrange(year, month)[1] + 1)]
        update_birthdate(e)
        page.update()
    
    day_dropdown = ft.Dropdown(
            label="Día",
            options=[ft.dropdown.Option(i) for i in range (1, 32)],
            width=control_width,
            value="" if user.birthdate is None else user.birthdate.day,
            on_change=update_birthdate,
            color="#33313D",
            label_style=ft.TextStyle(color="#D0D0D0"),
            border_color="#CC92AF"
        )
    
    month_dropdown = ft.Dropdown(
            label="Mes",
            options=[ft.dropdown.Option(calendar.month_abbr[i]) for i in range(1, 13)],
            on_change=on_month_year_change,
            width=control_width,
            value="" if user.birthdate is None else calendar.month_abbr[user.birthdate.month],
            color="#33313D",
            label_style=ft.TextStyle(color="#D0D0D0"),
            border_color="#CC92AF"
        )
    
    year_dropdown = ft.Dropdown(
            label="Año",
            options=[ft.dropdown.Option(i) for i in range(actual_year, actual_year - 80, -1)],
            on_change=on_month_year_change,
            width=control_width,
            value="" if user.birthdate is None else user.birthdate.year,
            color="#33313D",
            label_style=ft.TextStyle(color="#D0D0D0"),
            border_color="#CC92AF"
        )
    
    selector = ft.Row(
        controls=[day_dropdown, month_dropdown, year_dropdown],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )
    
    page.add(ft.Text("Fecha de nacimiento", color="#33313D", size=12), selector)
    
def add_contacts(page : ft.Page, user : UserData):
    def on_number_change(e):   
        new_val = e.control.value.replace(" ", "")
        index = int(e.control.label.replace("Contacto ", "")) - 1
        if len(new_val) != 10 or not new_val.isdecimal() or new_val in user.emergency_contacts:
            show_error_message(page, "Número de teléfono no válido")
            e.control.value = user.emergency_contacts[index]
            page.update()
            return
        
        
        user.emergency_contacts[index] = new_val
        save_user_data(user)
        
    page.add(ft.Text("Tus contactos de emergencia", size=12, color="#33313D"))
    for i in range(1,6):
        page.add(ft.TextField(label=f"Contacto {i}", value=user.emergency_contacts[i - 1], on_blur=on_number_change, label_style=ft.TextStyle(color="#D0D0D0"), border_color="#CC92AF", color="#33313D"))

def add_allergies(page : ft.page, user : UserData):
    def on_allergies_change(e):
        if not allergy_box.value.isalpha():
            show_error_message(page, "Coloca solo palabras")
            allergy_box.value = user.allergies
            
        update_user_field(user, "allergies", allergy_box.value)
        
    page.add(ft.Text("Tus alergias", size=12, color="#33313D"))
    allergy_box = ft.TextField(
        label="Alergias",
        value=user.allergies,
        on_blur=on_allergies_change,
        label_style=ft.TextStyle(color="#D0D0D0"),
        border_color="#CC92AF",
        color="#33313D")
    
    page.add(allergy_box)
       
def main(page : ft.Page):
    
    user = try_get_user_data()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    add_labels(page, user)
    add_birthdate_sel(page, user)
    add_allergies(page, user)
    add_contacts(page, user)
    page.update()
    
def try_get_user_data() -> UserData:
    try:
        return load_user_data()
    except Exception:
        user = UserData(
            "",
            None,
            "",
            "",
            0,
            0,
            "",
            ["" for _ in range(5)]
        )
        save_user_data(user)
        return user
    
def update_user_field(user : UserData, field : str, new_val : any):
    
    match field:
        case "name":
            if user.name == new_val:
                return
            user.name = new_val
        case "birth":
            if user.birthdate == new_val:
                return
            user.birthdate = new_val
        case "phone":
            if user.phone_number == new_val:
                return
            user.phone_number = new_val
        case "blood":
            if user.blood_type == new_val:
                return
            user.blood_type = new_val
        case "height":
            if user.height== new_val:
                return
            user.height = new_val
        case "weight":
            if user.weigth == new_val:
                return
            user.weigth = new_val
        case "allergies":
            if user.allergies == new_val:
                return
            user.allergies = new_val
            
    print(f"Updated {field} to {new_val}")
            
    save_user_data(user)

def show_error_message(page : ft.Page, message : str):
    errDialog = ft.AlertDialog(
                title=ft.Text(message),
                actions=[
                    ft.TextButton("Aceptar", on_click=lambda e:page.close(errDialog))
                ]
            )
    page.open(errDialog)