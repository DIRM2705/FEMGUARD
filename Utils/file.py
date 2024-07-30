MAIN_DIRECTORY = "FEMGUARD/"
VIDEO_DIRECTORY = "VIDEO/"

def add_data_to_file(data : bytearray, filename : str):
    route = get_video_route(filename)
    with open(route, "ab") as file:
        file.write(data)
        
def get_video_route(filename : str) -> str:
    return f"{MAIN_DIRECTORY}{VIDEO_DIRECTORY}{filename}.raw"