from homeassistant_api import Client
import secret

ha_ip_addr = '10.11.22.52'


def get_current(room, sensor):
    entity_id = f'sensor.psoc6_micropython_sensornode_{room}_{sensor}'
    r = 0.0
    try:
        with Client(
            f'http://{ha_ip_addr}:8123/api',
            secret.ha_access_token
        ) as client:

            entity = client.get_entity(entity_id=entity_id)

            return float(entity.get_state().state)
    except:
        if sensor == "atmospheric_pressure":
            r = 1000
        elif sensor == "relative_humidity":
            r = 50
        elif sensor == "co2_ppm":
            r = 500
        elif sensor == "temperature":
            r = 21
    return r
