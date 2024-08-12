import flet as ft
from Utils.file import get_video_files_list

def main(page : ft.Page):
    vidlist = get_video_files_list()
    page.add(make_title())
    if len(vidlist) > 0:
        for vid in vidlist:
            row = make_vid_bttn(vid)
            page.add(row)
    else:
        page.add(ft.Text("No hay videos aún"))

def make_title():
    return ft.Row(
        controls=[
            ft.Text("Videos grabados", size=25, color="#CB568D", weight=ft.FontWeight.BOLD)
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

def make_vid_bttn(vid_name : str) -> ft.CupertinoButton:
    row = ft.Row(
        controls=[
            ft.Icon(ft.icons.VIDEO_FILE_OUTLINED, color="#CB568D"),
            ft.Text(vid_name.removesuffix(".raw"), color="Black", size=20)
            ]
    )
    
    return ft.CupertinoButton(content=row, tooltip="Ir al video", bgcolor="#efbcce", padding=ft.padding.only(5,0,0,0))