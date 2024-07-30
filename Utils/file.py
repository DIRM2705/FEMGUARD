import datetime
import os

MAIN_DIRECTORY = "FEMGUARD/"
VIDEO_DIRECTORY = "VIDEO/"

def make_video(sender, data : bytearray):
    '''
    Función que se llama cuando comienza la grabación de video.
    Pasa los datos recolectados por el sensor de cámara a un archivo .raw
    '''
    route = get_video_route()
    with open(route, "ab") as file:
        file.write(data)
        
def get_video_route() -> str:
    now = datetime.datetime.now()
    date = now.strftime("%d%m%y")
    directory = f"{MAIN_DIRECTORY}{VIDEO_DIRECTORY}"
    video_index = len(os.listdir(directory))
    
    return f"{directory}FVID-{video_index}-{date}.raw"