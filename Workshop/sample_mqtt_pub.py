from umqtt.simple import MQTTClient
import time

# Test message subscription using mosquitto_sub
# mosquitto_sub -h <MQTT_BORKER_IP> -m "sensors/1/temperature"

MQTT_BROKER_IP="192.168.0.5"
STATION_NO=1
SENSOR_ID="TEMP_1"

def setup_mqtt_publisher():
    global mqtt_publisher

    mqtt_publisher = MQTTClient("umqtt_client", MQTT_BROKER_IP)
    mqtt_publisher.connect()

def publish_temp(pTemp):
    publish_time = time.localtime()
    #publish_time = time.localtime()
    output_str = "{Time: %s, Station: %d, Sensor: %s, Temp: %d}" % (publish_time, STATION_NO, SENSOR_ID, pTemp)
    mqtt_publisher.publish(b"sensors/1/temperature", output_str.encode('ascii'))

def main():
    setup_mqtt_publisher()
    for i in range(10):
        publish_temp(86)
        time.sleep(1)
    pass

if __name__ == "__main__":
    main()
