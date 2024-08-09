import flet as ft
from Utils.file import get_video_files_list

def main(page : ft.Page):
    vidlist = get_video_files_list()
    if len(vidlist) > 0:
        for vid in vidlist:
            row = make_vid_info_row(vid)
            page.add(row)
    else:
        page.add(ft.Text("No hay videos aún"))

def make_vid_info_row(vid_name : str) -> ft.Row:
    return ft.Row(
        controls=[
            ft.Icon(ft.icons.VIDEO_FILE_OUTLINED, color="#DC92B5"),
            ft.Text(vid_name.removesuffix(".raw"), color="Black")
            ]
    )