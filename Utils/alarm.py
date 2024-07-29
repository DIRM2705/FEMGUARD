from Utils.ble import BLE
            
def cancel_alarm(ble : BLE):
    '''
    Función para cancelar la alarma, escribe en el canal de comunicación del collar el nivel de alerta como bajo,
    abre la pantalla inicial y cierra la pantalla del botón cancelar
    
    Parámetros:     ble - El cliente bluetooth de la app
    '''
    print("Alarma cancelada")
    