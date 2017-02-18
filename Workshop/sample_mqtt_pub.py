from umqtt.simple import MQTTClient

MQTT_BROKER_IP="192.168.0.5"
STATION_NO=1
SENSOR_ID="TEMP_1"

def setup_mqtt_publisher():
    global mqtt_publisher

    mqtt_publisher = MQTTClient("umqtt_client", MQTT_BROKER_IP)
    mqtt_publisher.connect()

def publish_temp(pTemp):
    output_str = "{Station: %d, Sensor: %s, Temp: %d}" % (STATION_NO, SENSOR_ID, pTemp)
    mqtt_publisher.publish(b"sensors/temperature", output_str.encode('ascii'))
