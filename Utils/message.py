import os
from twilio.rest import Client

_TEMPLATE_MESSAGE = '''
    Mensaje de FEMGUARD
SOS: {} necesita asistencia.
Su ubicación actual es google.com.mx/maps/place/{},{}.
Llama a los servicios de emergencia cuanto antes.
''' 

_TWILIO_SSID = os.environ["TWILIO_SSID"]
_AUTH_TOKEN = os.environ["TWILIO_AUTH"]
_SENDER = os.environ["TELEPHONE"]

                    
def send_SOS_message(name : str, emergency_numbers : list[str], location : tuple[float, float]):
    '''
    Crea un cliente de Twilio y se conecta al servidor.
    Envía el mensaje de asistencia a todos los contactos de emergencia
    
    Parámetros:     name - El nombre del usuario
                    emergency_numbers - Los números de los contactos seleccionados por el usuario
                    location - La latitutud y longitud de la posición (obtenidas del geolocalizador de flet) 
    '''
    twilio_client = Client(_TWILIO_SSID, _AUTH_TOKEN)
    for number in emergency_numbers:
        twilio_client.messages.create(
            #Poner los datos del usuario en el mensaje a enviar
            body=_TEMPLATE_MESSAGE.format(name, location[0], location[1]),
            from_=_SENDER,
            to=number
        )