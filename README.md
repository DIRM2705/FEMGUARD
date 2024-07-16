<h1> FEMGUARD APP </h1>

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