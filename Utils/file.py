import datetime
import pickle
import os

MAIN_DIRECTORY = "FEMGUARD/"
CLIENT_FILE_NAME = "client.cfg"
USER_FILE_NAME = "user.cfg"
VIDEO_DIRECTORY = "VIDEO/"

def save_user_data(user):
    '''
    Guarda en un archivo los datos del usuario para su carga posterior
    '''
    check_route(MAIN_DIRECTORY)
    user_file = open(f"{MAIN_DIRECTORY}{USER_FILE_NAME}", "wb")
    pickle.dump(user, user_file)
    user_file.close()
    
def load_user_data():
    '''
    Carga los datos del usuario desde el archivo
    '''
    check_route(MAIN_DIRECTORY)
    user_file = open(f"{MAIN_DIRECTORY}{USER_FILE_NAME}", "rb")
    user = pickle.load(user_file)
    user_file.close()
    return user

def save_ble_client(client):
    '''
    Función que guarda un archivo el cliente BLE para su carga posterior
    '''
    check_route(MAIN_DIRECTORY)
    client_file = open(f"{MAIN_DIRECTORY}{CLIENT_FILE_NAME}", "wb")
    pickle.dump(client, client_file)
    client_file.close()

def load_ble_client():
    '''
    Función que crea un cliente BLE desde el archivo
    '''
    check_route(MAIN_DIRECTORY)
    client_file = open(f"{MAIN_DIRECTORY}{CLIENT_FILE_NAME}", "rb")
    client = pickle.load(client_file)    
    client_file.close()
    return client

def make_video(sender, data : bytearray):
    '''
    Función que se llama cuando comienza la grabación de video.
    Pasa los datos recolectados por el sensor de cámara a un archivo .raw
    '''
    print("file")
    route = get_video_route()
    with open(route, "ab") as file:
        file.write(data)
        
def get_video_files_list() -> list[str]:
    '''
    Obtiene todos los archivos de un video y guarda sus nombres en una lista
    
    retorna : lista con los nombres de los archivos
    '''
    route = f"{MAIN_DIRECTORY}{VIDEO_DIRECTORY}"
    check_route(route)
    return os.listdir(route)
        
def get_video_route() -> str:
    now = datetime.datetime.now()
    date = now.strftime("%d%m%y")
    directory = f"{MAIN_DIRECTORY}{VIDEO_DIRECTORY}"
    check_route(directory)
    video_index = 1#len(os.listdir(directory))
    
    return f"{directory}FVID-{video_index}-{date}.raw"

def check_route(route : str):
    if not os.path.exists(route):
        os.makedirs(route)