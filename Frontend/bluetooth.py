import flet as ft
from Utils.ble import BLE
from Exceptions import btExc
from Utils import file
from Utils.alarm import Alarm

async def add_device_buttons(e :ft.ControlEvent):
    page_text = ft.Text("Buscando dispositivos", color="#33313D")
    update_bttn = ft.IconButton(icon=ft.icons.REFRESH, icon_color="#D0D0D0", on_click=add_device_buttons, disabled=True)
    info_row = ft.Row(
            controls=[
                page_text,
                update_bttn
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    progress_ring = ft.ProgressRing(color="#E1BFD0")
    
    e.page.clean()
    e.page.add(info_row, progress_ring)
    
    devices = await ble.get_nearby_devices()
    
    e.page.remove(progress_ring)
    if ble.has_devices():
        page_text.value = "Dispositivos cercanos"
        for device in devices:
            e.page.add(make_connection_bttn(device, e.page.width))
    else:
        page_text.value = "No se encontraron dispositivos"
        
    update_bttn.disabled = False
    update_bttn.icon_color = "#CB568D"
    e.page.update()

ble : BLE = None

async def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    global ble
    ble = BLE.load_from_file()
    event = ft.ControlEvent("None", "Event", "", None, page)
    await add_device_buttons(event)
    page.update()
        

def make_connection_bttn(device_name : str, width : float):
    return ft.ElevatedButton(
            adaptive=True,
            bgcolor="#F9E7F1",
            width=width,
            height=50, 
            content=ft.Row(
                [
                    ft.Icon(name=ft.icons.BLUETOOTH, color="blue"),
                    ft.Text(device_name),
                ], 
                tight=True
            ),
            on_click=connect_to_device
    )
    
async def connect_to_device(e):
    device_name = e.control.content.controls[1].value
    
    dialog = ft.AlertDialog(
                actions=[
                    ft.TextButton("Aceptar", on_click=lambda e:e.page.close(dialog))
                ]
            )
    progress_ring = ft.ProgressRing(color="#E1BFD0")
    e.page.add(progress_ring)
    try:
        await ble.connect_to_device(device_name)
        await ble.subscribe_to_alerts()
        Alarm.ble = ble
        dialog.title = ft.Text(f"Te conectaste a {device_name} con éxito")
        ble.save()
    except btExc.ConnectionUnsuccessfullException as err:
        dialog.title = ft.Text(err)
    
    e.page.remove(progress_ring)
    e.page.open(dialog)
        
    