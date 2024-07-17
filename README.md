<h1> FEMGUARD APP </h1>

<h2> Preparación de entorno de desarrollo </h2>

Comienza creando una carpeta dónde guardarás los archivos de tu aplicación. Si tienes la consola de git instalada, puedes dar clic derecho sobre la carpeta que acabas de crear y buscar la opción **git bash here** eso abrirá un nueva consola de git.

Ejecuta lo siguiente en la consola:

```
git init
git clone https://github.com/DIRM2705/FEMGUARD-APP.git
```
Eso debería copiar todos los archivos del repositorio a la carpeta que acabas de crear.

Es necesaria la versión 3.12.4 de Python para seguir adelante, puedes conseguirla [aquí](https://www.python.org/downloads/)

Una vez que ya esté instalada la versión de Python correspondiente, deberás crear un entorno virtual. Para ello, ejecuta el siguiente comando en tu CMD:

```
py -m venv venv
```

Eso creará una carpeta llamada venv en tu locación actual que tendrá los archivos que conforman tu entorno virutal. Para activarlo copia el siguiente comando:

```
venv/Scripts/activate
```
Si el comando anterior no generó ningún error, el entorno virtual se ha activado con éxito.

Finalmente, deberás instalar los paquetes y dependencias, para ello necesitas descargar el archivo [requirements.txt]() del repositorio, además de ejecutar lo siguiente:

```
pip install -r requirements.txt
```

<h2> Bluetooth </h2>
<h3> Cliente Bluetooth Low-Energy </h3>

> class BLE()

Cliente bluetooth low energy de la aplicación.
- Buscará dispositivos cercanos,
- Conectará con dispositivos BLE que cumplan las características:
    - Tienen la UUID de alerta inmediata
- Se suscribirá a las notificaciones enviadas por el dispositivo de seguridad

> property BLE.callback : function(sender: BleakGATTCharacteristic, data: bytearrays)

La función que se ejecutará cuando la aplicación reciva una alerta inmediata.
La función puede o no ser asíncrona, no debe retornar nada y debe tener únicamente dos parámetros:
- `sender` de tipo [BleakGATTCharacteristic](https://bleak.readthedocs.io/en/latest/api/index.html#bleak.backends.characteristic.BleakGATTCharacteristic)
- `data` que es un arreglo de bytes

> async BLE.get_nearby_devices() → list[str]

Busca todos los dispositivos BLE cercanos,selecciona únicamente los que cumplan con las características preestablecidas y crea una lista con sus nombres

**Retorna:** Una lista que contiene los nombres de los dispositivos cercanos
        
> async BLE.connect_to_device(device : str)

Conecta la aplicación al dispositivo BLE `device`.

Arroja `ConnectionUnsuccessfullException` si no ha encontrado el dispositivo o el nombre del dispositivo ya no aparece en la lista de dipositivos disponibles.

**Parámetros:** **device** -  El nombre del dispositivo BLE al que se desea conectar.

> async BLE.connect_to_last_device()

Conecta la aplicación al último dispositivo BLE que se conectó.

Arroja `ConnectionUnsuccessfullException` si no encuentra el dispositivo o el cliente no ha estado conectado anteriormente.
    
> async BLE.subscribe_to_alert()

Pone la aplicación a esperar en segundo plano que el dispositivo vinculado produzca alertas inmediatas.

> async BLE.dismiss_alert()

Cambia el nivel de alerta a `No Alert` en la característica, `Alert Level` del dispositivo.

> async BLE.has_devices() → bool

Revisa si la aplicación ha encontrado algún dispositivo cercano

**Retorna:** Verdadero si hay se ha encontrado al menos un dispositivo

<h3> Excepciones </h3>

> exception ConnectionUnsuccessfullException

Excepción arrojada cuando ha habido algún error en la conexión bluetooth.