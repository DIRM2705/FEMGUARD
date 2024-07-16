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

<h2> Backend </h2>
<h3> Bluetooth </h3>

> async get_nearby_devices() -> list[BLEDevice]

Busca todos los dispositivos BLE cercanos,selecciona únicamente los que cumplan con lo siguiente:

- Incluye la UUID para immediate alert (alerta inmediata)

y crea una lista con ellos.

**Retorna:** Una lista de objetos [BLEDevice](https://bleak.readthedocs.io/en/latest/api/index.html#bleak.backends.device.BLEDevice).
        
> async connect_to_device(device : BLEDevice) -> BleakClient

Conecta la aplicación al dispositivo BLE `device`

**Parámetros:** **device** -  El dispositivo BLE al que se desea conectar (Idealmente el collar).

**Retorna:** Un nuevo cliente bluetooth asociado a los dispositivos conectados.
    
> async subscribe_to_alert(client : BleakClient):

Pone la aplicación a esperar en segundo plano que el dispositivo vinculado (collar) produzca alertas inmediatas.

**Parámetros:** **client** - El cliente bluetooth asociado a los dispositivos conectados